---
title: AI Assistant Live
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
license: mit
---

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
git clone https://github.com/artistica-004/ai-assistant-project.git
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

Built by Artistica-004

---

**Note**: This project uses free API tiers. For production use, consider upgrading to paid plans.

## 🔗 Links

- **GitHub**: https://github.com/artistica-004/ai-assistant-project
- **Live Demo**: https://huggingface.co/spaces/artistica-004/ai-assistant-live