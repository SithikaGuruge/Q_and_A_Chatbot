## 📚 Project Overview: FAQ Chatbot using LangChain, Gemini, FAISS & Streamlit

This project is an **AI-powered FAQ chatbot** built using **LangChain**, **Google PaLM (Gemini) LLM**, **FAISS** vector database, and **Streamlit**. The chatbot allows users to upload a CSV file containing frequently asked questions and their answers. After uploading, users can ask related questions, and the chatbot will intelligently respond by understanding the context of the data provided.

### 🔍 Key Features
- **Upload a CSV** containing FAQs (questions and answers).
- Ask follow-up or related questions in natural language.
- The chatbot retrieves relevant answers using semantic search and LLM reasoning.
- Fully interactive frontend powered by Streamlit.

### 🧠 Tech Stack
- **LangChain** – Framework to orchestrate LLMs and retrieval.
- **Google PaLM (Gemini)** – LLM for generating responses.
- **FAISS** – Fast and scalable vector search for document retrieval.
- **Streamlit** – Web interface for user interaction.
- **Google Generative AI Embeddings** – To embed question data into vector space.

### 🛠 How It Works
1. User uploads a `.csv` file containing a list of FAQ entries (with `prompt` and `response` columns).
2. The CSV is loaded and converted into vector embeddings using Google’s embedding model.
3. A FAISS vector store is built for fast retrieval.
4. When the user asks a question, the system retrieves the most relevant context from the vector store.
5. The question and retrieved context are passed to the Gemini LLM via a LangChain retrieval chain.
6. The model generates a context-aware answer and displays it via the Streamlit UI.

### 🧪 Example Use Case
You upload a CSV with entries like:
- **Prompt:** How can I reset my password?  
- **Response:** You can reset your password by clicking "Forgot Password" on the login screen.

You can then ask:  
> *“What should I do if I forgot my login credentials?”*

And the bot will answer based on the relevant data.

[Read my Medium article for more information](https://medium.com/@sithikaguruge2001/building-an-faq-chatbot-with-langchain-google-palm-llm-faiss-streamlit-3bdc8e16a4f6)

