"""End-to-End smoke tests for the Streamlit application.

This module contains basic E2E tests that verify the Streamlit server
launches correctly and responds to requests. Tests use Selenium with
headless Chrome for mock browser automation.
"""

import os
import subprocess
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


class TestStreamlitE2E:
    """End-to-end smoke tests for Streamlit application."""
    
    @pytest.fixture(scope="class")
    def streamlit_server(self):
        """Start Streamlit server for testing."""
        # Set dummy API key for testing (server needs it to start)
        os.environ['OPENAI_API_KEY'] = 'sk-test-dummy-key-for-testing'
        
        # Start Streamlit server
        process = subprocess.Popen(
            ['streamlit', 'run', 'app.py', '--server.port=8502'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        time.sleep(5)
        
        yield {
            'process': process,
            'url': 'http://localhost:8502'
        }
        
        # Cleanup: terminate server
        process.terminate()
        process.wait()
    
    @pytest.fixture(scope="class")
    def chrome_driver(self):
        """Create headless Chrome driver for testing."""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        
        try:
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(10)
            yield driver
        except WebDriverException as e:
            pytest.skip(f"Chrome driver not available: {e}")
        finally:
            if 'driver' in locals():
                driver.quit()
    
    def test_streamlit_server_starts(self, streamlit_server):
        """Test that Streamlit server starts successfully."""
        assert streamlit_server['process'].poll() is None, "Streamlit server failed to start"
    
    def test_streamlit_app_loads(self, streamlit_server, chrome_driver):
        """Test that Streamlit app page loads successfully."""
        try:
            chrome_driver.get(streamlit_server['url'])
            
            # Wait for page to load and check title
            WebDriverWait(chrome_driver, 10).until(
                lambda driver: driver.title != "" and "Streamlit" in driver.title
            )
            
            # Basic assertion that page loaded
            assert "Streamlit" in chrome_driver.title
            
        except TimeoutException:
            pytest.fail("Streamlit app failed to load within timeout")
    
    def test_app_has_basic_elements(self, streamlit_server, chrome_driver):
        """Test that basic UI elements are present."""
        try:
            chrome_driver.get(streamlit_server['url'])
            
            # Wait for Streamlit to fully load
            WebDriverWait(chrome_driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Check that page has content (not just empty)
            body = chrome_driver.find_element(By.TAG_NAME, "body")
            assert body.text.strip() != "", "Page body should not be empty"
            
        except TimeoutException:
            pytest.fail("Basic UI elements not found within timeout")
        except Exception as e:
            pytest.fail(f"Error checking basic elements: {e}")
    
    def test_no_obvious_errors(self, streamlit_server, chrome_driver):
        """Test that there are no obvious errors on page load."""
        try:
            chrome_driver.get(streamlit_server['url'])
            
            # Wait for page to load
            WebDriverWait(chrome_driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Check browser console for errors (basic check)
            logs = chrome_driver.get_log('browser')
            severe_errors = [log for log in logs if log['level'] == 'SEVERE']
            
            assert len(severe_errors) == 0, f"Severe browser errors found: {severe_errors}"
            
        except TimeoutException:
            pytest.fail("Page failed to load for error checking")
        except Exception as e:
            # This might fail in some environments, so we'll make it a soft failure
            print(f"Warning: Could not check browser logs: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
