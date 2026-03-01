# 🤖 Live AI Assistant

A powerful AI assistant that can search the web in real-time and provide accurate, up-to-date information.

## ✨ Features

- 💬 **Natural Conversations** - Chat naturally with AI
- 🔍 **Real-Time Web Search** - Searches Google for current information
- 🌤️ **Weather Updates** - Get current weather for any city
- 📰 **Latest News** - Fetch recent news and updates
- 🧠 **Memory** - Remembers conversation context
- ⚡ **Fast Responses** - Powered by Groq's high-speed AI

## 🛠️ Technology Stack

- **AI Model**: Groq Llama 3.3 70B
- **Web Search**: Google Search via SerpAPI
- **Framework**: Streamlit
- **Language**: Python 3.13

## 🚀 How It Works

1. User asks a question
2. AI determines if web search is needed
3. If yes, searches Google for latest information
4. AI processes search results
5. Provides accurate, real-time answer

## 💻 Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-assistant-project.git
cd ai-assistant-project

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your API keys
GROQ_API_KEY=your_groq_key
SERPAPI_KEY=your_serpapi_key

# Run the app
streamlit run app.py
```

## 🔑 API Keys Required

- **Groq API Key**: Get from [console.groq.com](https://console.groq.com)
- **SerpAPI Key**: Get from [serpapi.com](https://serpapi.com)

Both services offer free tiers!

## 📸 Screenshots

*Add screenshots here after deployment*

## 🎯 Use Cases

- Get real-time weather information
- Check latest news and updates
- Ask about current events
- Get sports scores
- Check stock prices
- General knowledge questions

## 🤝 Contributing

Feel free to fork this project and submit pull requests!

## 📄 License

MIT License

## 👨‍💻 Author

Built by [Your Name]

---

**Note**: This project uses free API tiers. For production use, consider upgrading to paid plans.
```

**3. Save the file** (Ctrl+S)

---

# 📝 STEP 2: Update .gitignore (Security!)

**1. Open `.gitignore` file**

**2. Make sure it has this:**
```
.env
__pycache__/
*.pyc
.streamlit/
*.log
.DS_Store