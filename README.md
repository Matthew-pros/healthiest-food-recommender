# Healthiest Food Recommender

A Streamlit-powered AI application that analyzes restaurant menu photos and text to recommend the healthiest food options using OpenAI's GPT-4o model. This application is a clone of the AI-powered "healthiest food recommender" app demonstrated in an Instagram reel by @heysirio (August 13, 2025).

## 🚀 Features

- **Photo Analysis**: Upload restaurant menu photos for AI-powered analysis
- **Text Input**: Enter menu items as text for quick recommendations
- **AI-Powered Recommendations**: Uses OpenAI's GPT-4o model (simulating GPT-5) for intelligent food analysis
- **Nutritional Insights**: Provides detailed explanations including calories, macros, vitamins, and health benefits
- **User-Friendly Interface**: Clean, intuitive Streamlit interface for seamless interaction

## 🏗️ Architecture

This application is built using:
- **Frontend**: Streamlit for the web interface
- **AI Backend**: OpenAI API (GPT-4o model)
- **Image Processing**: Built-in image upload and processing capabilities
- **Deployment**: Supports Streamlit Cloud and Heroku deployment

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key (requires paid account)
- Git (for cloning the repository)

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Matthew-pros/healthiest-food-recommender.git
cd healthiest-food-recommender
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup

#### Option A: Using Environment Variables
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

#### Option B: Using Streamlit Secrets (Recommended for deployment)
Create `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

**Note**: Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys). A paid OpenAI account is required.

## 🚀 Running the Application

### Local Development
```bash
streamlit run app.py
```
Then open your browser and navigate to `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account
2. **Connect to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your forked repository
3. **Configure Secrets**:
   - In Streamlit Cloud dashboard, go to your app settings
   - Add `OPENAI_API_KEY` in the secrets manager
   - Paste your OpenAI API key as the value
4. **Deploy**: Your app will be automatically deployed and accessible via a public URL

### Heroku Deployment (Optional)

1. **Install Heroku CLI** and login:
```bash
heroku login
```

2. **Create Heroku app**:
```bash
heroku create your-app-name
```

3. **Set environment variables**:
```bash
heroku config:set OPENAI_API_KEY=your_openai_api_key_here
```

4. **Deploy**:
```bash
git push heroku main
```

**Note**: Ensure you have a `Procfile` in your root directory for Heroku deployment.

## 📖 Usage Instructions

### Example Usage Scenarios

1. **Photo Upload**:
   - Click "Upload menu photo"
   - Select a clear image of a restaurant menu
   - Wait for AI analysis and recommendation

2. **Text Input**:
   - Enter menu items in the text box, such as:
     ```
     Cheeseburger, Grilled Chicken Salad, French Fries, Caesar Salad
     ```
   - Click "Get Recommendation"
   - Receive detailed analysis and health recommendation

### Expected Output Example
```
Recommended: Grilled Chicken Salad

Reason: This option provides high-quality protein (25-30g), essential vitamins from leafy greens, and is relatively low in calories (300-400 calories without dressing). The grilled preparation method avoids excess oils, and the vegetables provide fiber, folate, and antioxidants.

Tip: Request dressing on the side and choose vinaigrette over creamy dressings for optimal health benefits.
```

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Verify your OpenAI API key is correctly set
   - Ensure your OpenAI account has available credits
   - Check that the key has proper permissions

2. **Import Errors**:
   - Confirm all dependencies are installed: `pip install -r requirements.txt`
   - Verify Python version compatibility (3.10+)

3. **Image Upload Issues**:
   - Ensure uploaded images are in supported formats (JPG, PNG, etc.)
   - Check image file size limitations
   - Verify image quality and readability

4. **Deployment Issues**:
   - For Streamlit Cloud: Check that secrets are properly configured
   - For local deployment: Verify environment variables are set
   - Ensure all required files are committed to the repository

## 🔐 Security Notes

- **API Key Protection**: Never commit API keys to version control
- **Environment Variables**: Use secure methods to store sensitive credentials
- **Access Control**: Consider implementing user authentication for production use
- **Rate Limiting**: Be aware of OpenAI API rate limits and implement appropriate handling
- **Data Privacy**: User-uploaded images are processed but not stored permanently

## 🤝 Customization Ideas

- Add order confirmation simulation after recommendation
- Implement user preferences (dietary restrictions, allergies)
- Add nutritional database integration
- Include meal planning features
- Add multiple language support
- Implement user feedback and rating system

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original concept inspired by @heysirio's Instagram demonstration (August 13, 2025)
- Built with Streamlit and OpenAI's powerful GPT-4o model
- Thanks to the open-source community for continuous support

## 🐛 Issues and Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review existing [GitHub Issues](https://github.com/Matthew-pros/healthiest-food-recommender/issues)
3. Create a new issue with detailed information about your problem

---

**Made with ❤️ using Streamlit and OpenAI API**
