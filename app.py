import streamlit as st
import base64
import os
from openai import OpenAI
from utils import validate_inputs  # Import from utils module

# Page configuration
st.set_page_config(
    page_title="Healthiest Food Recommender",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration and initialization
def get_openai_client():
    """Initialize OpenAI client with proper error handling"""
    api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY in secrets or environment variables.")
        st.stop()
    return OpenAI(api_key=api_key)

def get_model_name():
    """Get model name from secrets or environment, with fallback"""
    return (
        st.secrets.get("OPENAI_MODEL") or 
        os.environ.get("OPENAI_MODEL") or 
        "gpt-4o"
    )

# Note: validate_inputs function has been moved to utils.py for better testability

def format_nutrition_response(recommendation):
    """Format the recommendation with nutrition rubric structure"""
    st.subheader("🍽️ Nutritional Analysis & Recommendation")
    
    # Display recommendation in formatted sections
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Analysis Results")
        st.markdown(recommendation)
    
    with col2:
        st.markdown("### 🏆 Health Scoring Criteria")
        st.markdown("""
        **Evaluation Factors:**
        - 🔥 Calorie Content
        - 🥩 Protein Quality
        - 🌾 Fiber Content
        - 🍎 Vitamin Density
        - 🧂 Sodium Levels
        - 🍯 Sugar Content
        - 🥑 Healthy Fats
        - ⚖️ Nutritional Balance
        """)
        
        st.info("💡 **Tip**: Look for items with high protein, fiber, and vitamins while being moderate in calories and low in processed sugars.")

# Initialize client
try:
    client = get_openai_client()
    model_name = get_model_name()
except Exception as e:
    st.error(f"Failed to initialize: {str(e)}")
    st.stop()

# UI Header
st.title("🥗 Healthiest Food Recommender")
st.markdown("""
**AI-Powered Nutrition Analysis** 🤖
Upload a menu photo or enter menu items below. Our AI will analyze nutritional content 
and recommend the healthiest option based on comprehensive health factors.
""")

# Sidebar with instructions
with st.sidebar:
    st.header("📋 How to Use")
    st.markdown("""
    1. **Upload** a menu photo OR
    2. **Type** menu items manually
    3. **Click** analyze for recommendations
    
    **Supported formats**: JPG, PNG, JPEG
    **Max file size**: 10MB
    """)
    
    st.header("⚙️ Settings")
    st.info(f"**Model**: {model_name}")

# Main input section
col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Upload Menu Photo")
    uploaded_file = st.file_uploader(
        "Choose a menu image...",
        type=["jpg", "png", "jpeg"],
        help="Upload a clear photo of the menu for AI analysis"
    )
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Menu", use_column_width=True)

with col2:
    st.subheader("✏️ Or Enter Menu Items")
    menu_text = st.text_area(
        "Type menu items here...",
        placeholder="Example:\nBurger: 800 cal, beef patty, cheese, fries\nSalad: 300 cal, mixed greens, grilled chicken\nPasta: 600 cal, marinara sauce, parmesan",
        height=200,
        help="Enter menu items with descriptions and calories if available"
    )

# Analysis section
if st.button("🔍 Analyze and Recommend", type="primary", use_container_width=True):
    # Input validation using imported function
    is_valid, error_message = validate_inputs(uploaded_file, menu_text)
    
    if not is_valid:
        st.error(error_message)
        st.stop()
    
    # Show progress
    with st.spinner('🤔 Analyzing nutritional content...'):
        try:
            # Prepare enhanced prompt with nutrition rubric
            prompt = """
            Analyze the provided menu (from image or text). For each menu item:
            
            1. Extract all items with descriptions and nutritional info if available
            2. Evaluate each item based on:
               - Calorie content and portion appropriateness
               - Protein quality and quantity
               - Fiber content and complex carbohydrates
               - Vitamin and mineral density
               - Sodium levels and processing degree
               - Sugar content (added vs natural)
               - Healthy fat content
               - Overall nutritional balance
            
            3. Recommend the SINGLE healthiest option with:
               - Clear reasoning for the choice
               - Specific nutritional benefits
               - Suggested modifications for even better health
               - Brief comparison to other options
            
            Format your response clearly with sections for easy reading.
            """
            
            messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
            
            # Handle image upload
            if uploaded_file:
                try:
                    # Reset file pointer and encode image
                    uploaded_file.seek(0)
                    base64_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
                    messages[0]["content"].append({
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    })
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
                    st.stop()
            
            # Handle text input
            if menu_text:
                enhanced_prompt = prompt + f"\n\nMenu text provided:\n{menu_text}"
                messages[0]["content"][0]["text"] = enhanced_prompt
            
            # Make API call with improved error handling
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    max_tokens=800,
                    temperature=0.3  # Lower temperature for more consistent analysis
                )
                
                recommendation = response.choices[0].message.content
                
                if recommendation:
                    format_nutrition_response(recommendation)
                else:
                    st.error("No recommendation received. Please try again.")
                    
            except Exception as api_error:
                error_msg = str(api_error)
                if "insufficient_quota" in error_msg.lower():
                    st.error("🚫 API quota exceeded. Please check your OpenAI account credits.")
                elif "invalid_api_key" in error_msg.lower():
                    st.error("🔑 Invalid API key. Please check your OpenAI API key configuration.")
                elif "rate_limit" in error_msg.lower():
                    st.error("⏳ Rate limit reached. Please wait a moment and try again.")
                else:
                    st.error(f"🔧 API Error: {error_msg}")
                
                st.info("💡 **Troubleshooting**: Ensure your OpenAI API key is valid and has sufficient credits.")
                
        except Exception as general_error:
            st.error(f"❌ Unexpected error: {str(general_error)}")
            st.info("Please try again or contact support if the issue persists.")

# Footer
st.markdown("---")
st.markdown("""<div style="text-align: center; color: #666;">    🤖 Powered by OpenAI • 🥗 Promoting Healthy Choices • ⚡ Built with Streamlit</div>""", unsafe_allow_html=True)
