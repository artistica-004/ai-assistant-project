import streamlit as st
import os
from groq import Groq
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize clients
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Page configuration
st.set_page_config(
    page_title="Shivani's AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Shivani's Live AI Assistant")
st.markdown("*Powered by Groq AI + Real-Time Web Search*")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def search_web(query):
    """Search the web and return formatted results"""
    try:
        url = "https://serpapi.com/search"
        params = {
            "q": query,
            "api_key": SERPAPI_KEY,
            "engine": "google"
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return None
        
        data = response.json()
        
        if "error" in data:
            return None
        
        search_info = ""
        
        # Get answer box
        if "answer_box" in data:
            answer = data["answer_box"]
            if "answer" in answer:
                search_info += f"{answer['answer']}\n\n"
            if "snippet" in answer:
                search_info += f"{answer['snippet']}\n\n"
        
        # Get knowledge graph
        if "knowledge_graph" in data:
            kg = data["knowledge_graph"]
            if "description" in kg:
                search_info += f"{kg['description']}\n\n"
        
        # Get organic results
        if "organic_results" in data:
            for result in data["organic_results"][:3]:
                title = result.get("title", "")
                snippet = result.get("snippet", "")
                search_info += f"**{title}**\n{snippet}\n\n"
        
        return search_info if search_info else None
        
    except Exception as e:
        return None

def get_ai_response(user_message):
    """Get AI response with optional web search"""
    
    # Keywords that trigger web search
    search_keywords = [
        "weather", "temperature", "forecast",
        "news", "latest", "recent", "today", "current",
        "price", "cost", "stock", "who is", "what is",
        "when is", "where is", "how much"
    ]
    
    needs_search = any(keyword in user_message.lower() for keyword in search_keywords)
    
    search_results = ""
    if needs_search:
        with st.spinner("🔍 Searching the web..."):
            results = search_web(user_message)
            if results:
                search_results = f"\n\n--- WEB SEARCH RESULTS ---\n{results}--- END OF RESULTS ---\n"
    
    # Prepare messages
    system_msg = """You are a helpful AI assistant with web search capabilities.

INSTRUCTIONS:
- When web search results are provided between --- markers, use that information
- Provide direct, specific answers (temperatures, prices, dates, etc.)
- Don't suggest the user to check websites if you have the information
- Be conversational and helpful
- If no search results, use your general knowledge"""

    messages = [
        {"role": "system", "content": system_msg}
    ]
    
    # Add conversation history (last 10 messages)
    for msg in st.session_state.messages[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    # Add current message
    full_message = user_message + search_results
    messages.append({"role": "user", "content": full_message})
    
    try:
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display AI response
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.markdown(response)
    
    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("ℹ️ About This AI")
    st.markdown("""
    **Features:**
    - 💬 Natural conversation
    - 🔍 Real-time web search
    - 🌤️ Current weather info
    - 📰 Latest news
    - 🧠 Conversation memory
    - ⚡ Fast responses
    """)
    
    st.markdown("---")
    st.markdown("**Technology:**")
    st.markdown("- AI: Groq Llama 3.3 70B")
    st.markdown("- Search: Google (SerpAPI)")
    st.markdown("- Framework: Streamlit")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Built with ❤️ using AI")