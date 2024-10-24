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
Explore the world of search using LangChain with integrated tools like Arxiv, Wikipedia, and DuckDuckGo. Feel free to ask any question!

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

# Load the external CSS file
with open('styles.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
