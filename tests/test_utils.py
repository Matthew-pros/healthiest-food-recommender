"""Unit tests for utils.py functions.

This module contains unit tests for the utility functions used in the
Healthiest Food Recommender application.
"""

import pytest
from unittest.mock import Mock
from utils import validate_inputs


class TestValidateInputs:
    """Test cases for the validate_inputs function."""
    
    def test_validate_inputs_no_input_provided(self):
        """Test validation when no file or text input is provided."""
        result, message = validate_inputs(None, "")
        assert result is False
        assert message == "Please upload a menu photo or enter menu items."
        
    def test_validate_inputs_only_whitespace_text(self):
        """Test validation when only whitespace is provided as text."""
        result, message = validate_inputs(None, "   \n\t  ")
        assert result is False
        assert message == "Please upload a menu photo or enter menu items."
        
    def test_validate_inputs_valid_text_input(self):
        """Test validation with valid text input."""
        result, message = validate_inputs(None, "Pizza, Burger, Salad")
        assert result is True
        assert message == ""
        
    def test_validate_inputs_valid_file_input(self):
        """Test validation with valid file input."""
        mock_file = Mock()
        mock_file.size = 5 * 1024 * 1024  # 5MB
        
        result, message = validate_inputs(mock_file, "")
        assert result is True
        assert message == ""
        
    def test_validate_inputs_file_too_large(self):
        """Test validation when uploaded file is too large."""
        mock_file = Mock()
        mock_file.size = 15 * 1024 * 1024  # 15MB (exceeds 10MB limit)
        
        result, message = validate_inputs(mock_file, "")
        assert result is False
        assert message == "File size too large. Please upload a file smaller than 10MB."
        
    def test_validate_inputs_text_too_long(self):
        """Test validation when text input is too long."""
        long_text = "a" * 2001  # Exceeds 2000 character limit
        
        result, message = validate_inputs(None, long_text)
        assert result is False
        assert message == "Menu text too long. Please keep it under 2000 characters."
        
    def test_validate_inputs_both_file_and_text_valid(self):
        """Test validation when both valid file and text are provided."""
        mock_file = Mock()
        mock_file.size = 5 * 1024 * 1024  # 5MB
        
        result, message = validate_inputs(mock_file, "Pizza, Burger")
        assert result is True
        assert message == ""
        
    def test_validate_inputs_file_at_size_limit(self):
        """Test validation when file is exactly at the size limit."""
        mock_file = Mock()
        mock_file.size = 10 * 1024 * 1024  # Exactly 10MB
        
        result, message = validate_inputs(mock_file, "")
        assert result is True
        assert message == ""
        
    def test_validate_inputs_text_at_length_limit(self):
        """Test validation when text is exactly at the length limit."""
        text_at_limit = "a" * 2000  # Exactly 2000 characters
        
        result, message = validate_inputs(None, text_at_limit)
        assert result is True
        assert message == ""
        
    def test_validate_inputs_file_slightly_over_limit(self):
        """Test validation when file is slightly over the size limit."""
        mock_file = Mock()
        mock_file.size = (10 * 1024 * 1024) + 1  # 10MB + 1 byte
        
        result, message = validate_inputs(mock_file, "")
        assert result is False
        assert message == "File size too large. Please upload a file smaller than 10MB."
        
    def test_validate_inputs_file_has_text_too_long(self):
        """Test validation when file is valid but text is too long."""
        mock_file = Mock()
        mock_file.size = 5 * 1024 * 1024  # 5MB - valid
        long_text = "a" * 2001  # Too long
        
        result, message = validate_inputs(mock_file, long_text)
        assert result is False
        assert message == "Menu text too long. Please keep it under 2000 characters."
        
    def test_validate_inputs_file_too_large_has_valid_text(self):
        """Test validation when file is too large but text is valid."""
        mock_file = Mock()
        mock_file.size = 15 * 1024 * 1024  # 15MB - too large
        
        result, message = validate_inputs(mock_file, "Valid menu text")
        assert result is False
        assert message == "File size too large. Please upload a file smaller than 10MB."
        
    def test_validate_inputs_edge_cases(self):
        """Test various edge cases for input validation."""
        # Test with empty string vs None
        result1, _ = validate_inputs(None, "")
        result2, _ = validate_inputs(None, None)
        assert result1 is False
        # Note: The function expects a string, but if None is passed, 
        # it should handle gracefully in a real implementation
        
        # Test with minimal valid input
        result3, message3 = validate_inputs(None, "a")
        assert result3 is True
        assert message3 == ""
        
        # Test file size of 0
        mock_file = Mock()
        mock_file.size = 0
        result4, message4 = validate_inputs(mock_file, "")
        assert result4 is True
        assert message4 == ""


if __name__ == "__main__":
    pytest.main([__file__])
