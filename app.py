import streamlit as st
import base64
from openai import OpenAI
# Initialize OpenAI client (use your API key)
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", "your-api-key-here"))  # Replace with your key or use secrets in deployment
st.title("Healthiest Food Recommender App")
st.markdown("Upload a photo of a menu or enter menu items below. The AI will analyze and recommend the healthiest option based on nutrition, calories, balance, and overall health benefits.")
# Option 1: Upload image of menu
uploaded_file = st.file_uploader("Upload Menu Photo", type=["jpg", "png", "jpeg"])
# Option 2: Text input for menu items
menu_text = st.text_area("Or Enter Menu Items (e.g., 'Burger: 800 cal, Salad: 300 cal, Pasta: 600 cal')")
if st.button("Analyze and Recommend"):
    prompt = "Analyze the provided menu (from image or text). Extract all items with descriptions if available. Recommend the single healthiest option, explaining why based on factors like calories, protein, fiber, vitamins, low sugar/fat, and overall nutritional balance. Suggest any modifications for even better health if applicable."
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
    if uploaded_file:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Menu", use_column_width=True)
        
        # Encode image to base64
        base64_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
        messages[0]["content"].append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
        })
    
    if menu_text:
        # Append text to prompt if provided
        enhanced_prompt = prompt + f"\nMenu text: {menu_text}"
        messages[0]["content"][0]["text"] = enhanced_prompt
    
    if uploaded_file or menu_text:
        try:
            # Call OpenAI API (using gpt-4o for vision and reasoning; replace with 'gpt-5' if available)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=500
            )
            recommendation = response.choices[0].message.content
            st.subheader("Recommendation:")
            st.write(recommendation)
        except Exception as e:
            st.error(f"Error: {str(e)}. Check your API key and credits.")
    else:
        st.warning("Please upload a photo or enter menu items.")
