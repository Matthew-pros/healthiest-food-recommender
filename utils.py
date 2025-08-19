"""Utility functions for the Healthiest Food Recommender application.

This module contains utility functions that can be tested independently,
improving code maintainability and testability.
"""

def validate_inputs(uploaded_file, menu_text):
    """Validate user inputs for the food recommender application.
    
    Args:
        uploaded_file: Streamlit uploaded file object or None
        menu_text (str): Text input from user
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
               Returns (True, "") if inputs are valid,
               Returns (False, error_message) if inputs are invalid
               
    Examples:
        >>> validate_inputs(None, "")
        (False, "Please upload a menu photo or enter menu items.")
        
        >>> validate_inputs(None, "Pizza, Salad, Burger")
        (True, "")
    """
    if not uploaded_file and not menu_text.strip():
        return False, "Please upload a menu photo or enter menu items."
    
    if uploaded_file:
        if uploaded_file.size > 10 * 1024 * 1024:  # 10MB limit
            return False, "File size too large. Please upload a file smaller than 10MB."
    
    if menu_text and len(menu_text.strip()) > 2000:
        return False, "Menu text too long. Please keep it under 2000 characters."
    
    return True, ""
