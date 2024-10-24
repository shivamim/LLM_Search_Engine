🔎 LangChain Search Assistant - Streamlit App
This project is a search assistant built using LangChain and deployed on Streamlit. It integrates multiple search tools like Arxiv, Wikipedia, and DuckDuckGo to answer queries and retrieve information from academic papers, web resources, and more. The app is interactive and designed to provide relevant responses in real time.



🛠 Key Features:
Multisource Search: Combines search tools (Arxiv, Wikipedia, and DuckDuckGo) to give comprehensive and accurate answers.
Zero-Shot React Description Agent: Uses LangChain's agent to process queries with no pre-defined templates, handling a wide variety of questions.
Streaming Responses: Real-time streaming of long outputs for a smoother and faster user experience.
Customizable Output: Limits results from each source to provide focused answers (e.g., top 1 result from Arxiv and Wikipedia).
Seamless API Key Management: No user input for API keys required; keys are securely stored and managed via Streamlit secrets.


🖥️ UI Enhancements:
Clean and modern chat interface with distinct message styling for user and assistant responses.
Light background colors and clear margins for better readability and aesthetic appeal.


🚀 Getting Started:
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/langchain-search-assistant
cd langchain-search-assistant
Set up Environment:



Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Add API Keys:



Navigate to the Streamlit secrets section and add the following key:
bash
Copy code
GROQ_API_KEY = "your_groq_api_key_here"
Run the App:



Start the Streamlit app:
bash
Copy code
streamlit run app.py


📚 Tools and Libraries Used:
LangChain: For building language model applications and agent handling.
Streamlit: To create a fast and interactive web app.
Arxiv API Wrapper: Fetches academic research papers from the Arxiv repository.
Wikipedia API Wrapper: Fetches relevant articles from Wikipedia.
DuckDuckGo Search: For general web search integration.


📑 Project Structure:
app.py: Main application file for the Streamlit app.
requirements.txt: List of all dependencies for the project.
.streamlit/secrets.toml: Secure storage for API keys (ensure this is not tracked in Git).


🌱 Future Improvements:
Integration of additional search tools (e.g., Google Scholar).
Improved error handling for more seamless user interactions.
Enhanced model response capabilities for more complex queries.
