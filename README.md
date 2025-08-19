# Healthiest Food Recommender

[![CI](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/ci.yml/badge.svg)](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/ci.yml)
[![Pre-commit](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/precommit.yml/badge.svg)](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/precommit.yml)
[![Tests](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/test.yml/badge.svg)](https://github.com/Matthew-pros/healthiest-food-recommender/actions/workflows/test.yml)

A sophisticated Streamlit-powered AI application that analyzes restaurant menu photos and text to recommend the healthiest food options using OpenAI's GPT-4o model. This application is inspired by the AI-powered "healthiest food recommender" app demonstrated in an Instagram reel by @heysirio (August 13, 2025).

![Sample Menu Analysis](assets/sample-menu.jpg)

## ✨ Key Features

- **🖼️ Photo Analysis**: Upload restaurant menu photos for AI-powered analysis
- **📝 Text Input**: Enter menu items as text for quick recommendations
- **🧠 AI-Powered Recommendations**: Uses OpenAI's GPT-4o model for intelligent food analysis
- **📊 Nutritional Insights**: Provides detailed explanations including calories, macros, vitamins, and health benefits
- **🎨 User-Friendly Interface**: Clean, intuitive Streamlit interface for seamless interaction

## 🚀 Quick Start

```bash
# One-liner setup and run
git clone https://github.com/Matthew-pros/healthiest-food-recommender.git && cd healthiest-food-recommender && pip install -r requirements.txt && echo "OPENAI_API_KEY=your_key_here" > .env && streamlit run app.py
```

```bash
# Alternative: Using Streamlit secrets
git clone https://github.com/Matthew-pros/healthiest-food-recommender.git && cd healthiest-food-recommender && pip install -r requirements.txt && mkdir -p .streamlit && echo 'OPENAI_API_KEY = "your_key_here"' > .streamlit/secrets.toml && streamlit run app.py
```

## 🏗️ Architecture Overview

This application is built using modern technologies:

- **Frontend**: Streamlit for the web interface
- **AI Backend**: OpenAI API (GPT-4o model)
- **Image Processing**: Built-in image upload and processing capabilities
- **Deployment**: Supports Streamlit Cloud, Heroku, and local deployment

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key (requires paid account)
- Git (for cloning the repository)

## ⚙️ Detailed Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Matthew-pros/healthiest-food-recommender.git
cd healthiest-food-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

#### Option A: Using Environment Variables

Create a .env file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o
```

#### Option B: Using Streamlit Secrets (Recommended for deployment)

Create .streamlit/secrets.toml:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
OPENAI_MODEL = "gpt-4o"
```

**Note**: Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys). A paid OpenAI account is required.

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| OPENAI_API_KEY | Your OpenAI API key | - | ✅ |
| OPENAI_MODEL | OpenAI model to use | gpt-4o | ❌ |
| MAX_IMAGE_SIZE | Max image size in MB | 10 | ❌ |
| DEBUG_MODE | Enable debug logging | false | ❌ |

### Supported OpenAI Models

- gpt-4o (recommended)
- gpt-4-turbo
- gpt-4
- gpt-3.5-turbo

## 🚀 Running the Application

### Local Development

```bash
streamlit run app.py
```

Then open your browser and navigate to http://localhost:8501

## 🌐 Deployment Options

### Streamlit Cloud Deployment

1. Fork this repository to your GitHub account
2. Connect to Streamlit Cloud:
   - Visit [share.streamlit.io](https://share.streamlit.io/)
   - Connect your GitHub account
   - Select your forked repository
3. Configure Secrets:
   - In Streamlit Cloud dashboard, go to your app settings
   - Add OPENAI_API_KEY in the secrets manager
   - Add OPENAI_MODEL (optional)
   - Paste your OpenAI API key as the value
4. Deploy: Your app will be automatically deployed and accessible via a public URL

### Heroku Deployment

#### Prerequisites for Heroku

Ensure you have the following files in your repository:

**Procfile:**
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**runtime.txt:**
```
python-3.10.12
```

**setup.sh:**
```bash
#!/bin/bash
mkdir -p ~/.streamlit/
echo "\n[server]\n\nheadless = true\n\nport = $PORT\n\nenableCORS = false\n\n" > ~/.streamlit/config.toml
```

#### Deployment Steps

1. Install Heroku CLI and login:
   ```bash
   heroku login
   ```

2. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```

3. Set environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key_here
   heroku config:set OPENAI_MODEL=gpt-4o
   ```

4. Deploy:
   ```bash
   git push heroku main
   ```

## 📖 Usage Guide

### Getting Started

1. Launch the application using one of the methods above
2. Choose your input method:
   - Upload a menu photo, or
   - Enter menu items as text
3. Get AI-powered recommendations with detailed nutritional analysis

### Example Usage Scenarios

#### Photo Upload Method

1. Click "Upload menu photo"
2. Select a clear image of a restaurant menu (see [sample](assets/sample-menu.jpg))
3. Wait for AI analysis and recommendation

#### Text Input Method

1. Enter menu items in the text box, such as:
   ```
   Cheeseburger, Grilled Chicken Salad, French Fries, Caesar Salad
   ```
2. Click "Get Recommendation"
3. Receive detailed analysis and health recommendation

### Sample Output

```
Recommended: Grilled Chicken Salad

Reason: This option provides high-quality protein (25-30g), essential vitamins from leafy greens, and is relatively low in calories (300-400 calories without dressing). The grilled preparation method avoids excess oils, and the vegetables provide fiber, folate, and antioxidants.

Tip: Request dressing on the side and choose vinaigrette over creamy dressings for optimal health benefits.
```

## 🛠️ Troubleshooting Matrix

| Issue | Symptoms | Solution | Priority |
|-------|----------|----------|----------|
| API Key Errors | "Authentication failed", "Invalid API key" | • Verify API key is correct<br/>• Check account credits<br/>• Ensure proper permissions | 🔴 High |
| Import Errors | "ModuleNotFoundError", "ImportError" | • Run `pip install -r requirements.txt`<br/>• Check Python version (3.10+)<br/>• Try virtual environment | 🟡 Medium |
| Image Upload Issues | Upload fails, "Unsupported format" | • Use JPG/PNG formats<br/>• Check file size (<10MB)<br/>• Ensure image clarity | 🟡 Medium |
| Deployment Issues | App won't start, environment errors | • Verify secrets configuration<br/>• Check all files are committed<br/>• Review deployment logs | 🔴 High |
| Slow Response | Long loading times | • Check internet connection<br/>• Verify OpenAI API status<br/>• Try smaller images | 🟢 Low |
| Model Errors | "Model not found", API errors | • Check OPENAI_MODEL setting<br/>• Verify model availability<br/>• Try fallback model | 🟡 Medium |

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: Do I need a paid OpenAI account?**  
A: Yes, a paid OpenAI account with available credits is required to use the GPT-4o model.

**Q: What image formats are supported?**  
A: JPG, PNG, GIF, and WebP formats are supported. Images should be clear and readable for best results.

**Q: Can I use this app offline?**  
A: No, the app requires internet connection to communicate with OpenAI's API.

**Q: Is my uploaded data stored anywhere?**  
A: No, uploaded images and text are processed in real-time and not stored permanently.

### Technical Questions

**Q: Which OpenAI model should I use?**  
A: GPT-4o is recommended for best results. You can also use gpt-4-turbo or gpt-4 for good performance.

**Q: How do I change the AI model?**  
A: Set the OPENAI_MODEL environment variable to your preferred model (e.g., "gpt-4o", "gpt-4-turbo").

**Q: Why is the app slow?**  
A: Response time depends on image size, complexity, and OpenAI API load. Try using smaller, clearer images.

**Q: Can I customize the recommendations?**  
A: Yes, you can modify the prompts in app.py to customize the AI's analysis criteria and output format.

### Deployment Questions

**Q: Which deployment option is best?**  
A: Streamlit Cloud is recommended for simplicity. Heroku offers more control but requires additional configuration.

**Q: How do I update my deployed app?**  
A: For Streamlit Cloud: Push changes to your GitHub repository. For Heroku: Use `git push heroku main`.

**Q: Can I deploy this on other platforms?**  
A: Yes, the app can be deployed on any platform supporting Python and Streamlit (AWS, GCP, Azure, etc.).

## 🔐 Security Best Practices

- **API Key Protection**: Never commit API keys to version control
- **Environment Variables**: Use secure methods to store sensitive credentials
- **Access Control**: Consider implementing user authentication for production use
- **Rate Limiting**: Be aware of OpenAI API rate limits and implement appropriate handling
- **Data Privacy**: User-uploaded images are processed but not stored permanently
- **HTTPS**: Always use HTTPS in production environments
- **Input Validation**: The app includes built-in input validation and sanitization

## 🎯 Customization Ideas

- Add order confirmation simulation after recommendation
- Implement user preferences (dietary restrictions, allergies)
- Add nutritional database integration for more detailed analysis
- Include meal planning and tracking features
- Add multiple language support for international users
- Implement user feedback and rating system
- Add export functionality for recommendations
- Include calorie tracking and daily nutrition goals

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original concept inspired by @heysirio's Instagram demonstration (August 13, 2025)
- Built with Streamlit and OpenAI's powerful GPT-4o model
- Thanks to the open-source community for continuous support and contributions
- Special thanks to the Streamlit team for their amazing framework

## 🐛 Issues and Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting Matrix](#🛠️-troubleshooting-matrix) above
2. Review the [FAQ section](#❓-frequently-asked-questions-faq)
3. Check existing [GitHub Issues](https://github.com/Matthew-pros/healthiest-food-recommender/issues)
4. Create a new issue with detailed information about your problem
5. Include relevant logs, error messages, and system information

### Issue Template

When reporting issues, please include:

- **Environment**: OS, Python version, dependencies
- **Error message**: Full error traceback if available
- **Steps to reproduce**: How to recreate the issue
- **Expected behavior**: What should happen
- **Screenshots**: If applicable

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

**Made with ❤️ using Streamlit and OpenAI API**

⭐ **Star this repository if you find it helpful!**
