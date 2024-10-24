import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os

# Load API keys from Streamlit secrets
groq_api_key = st.secrets["GROQ_API_KEY"]

# Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# App Title and Description
st.title("🔎 Sarvavidya - Enhanced Search Assistant")
st.write("""
I am Sarvavidya (सर्वविद्या), your all-knowing guide to knowledge, helping you discover answers and insights from a variety of sources.
""")

# Session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I assist you today?"}
    ]

# Display previous messages in chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# Chat input and response
if prompt := st.chat_input(placeholder="Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize LLM with stored key
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role': 'assistant', "content": response})
        st.write(response)

# UI Enhancements
st.markdown("""
<style>
    body {
        background-image: url('https://pixabay.com/vectors/chatbot-bot-chat-robot-talk-6626193/');
        background-size: cover;
        background-position: center;
        color: #333; /* Default text color */
    }
    .st-chat-message {
        margin-bottom: 10px;
        border-radius: 10px; /* Rounded corners for chat messages */
        padding: 10px; /* Padding for chat messages */
    }
    .st-chat-message-user {
        background-color: #e8f0fe; /* User message background */
        color: #333; /* User message text color */
    }
    .st-chat-message-assistant {
        background-color: #e1f5fe; /* Assistant message background */
        color: #333; /* Assistant message text color */
    }
    .stTextInput input {
        background-color: #f9f9f9; /* Light background color */
        border: 2px solid #ccc; /* Light gray border */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Padding for comfort */
        font-size: 16px; /* Larger font size */
    }
</style>
""", unsafe_allow_html=True)
