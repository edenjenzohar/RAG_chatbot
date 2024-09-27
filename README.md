# RAG chatbot 🤖 using LangChain 🦜🔗

## Project Overview <a name="overview"></a>

Although Large Language Models (LLMs) are powerful and capable of generating creative content, they can produce outdated or incorrect information as they are trained on static data. To overcome this limitation, Retrieval Augmented Generation (RAG) systems can be used to connect the LLM to external data and obtain more reliable answers.

The aim of this project is to build a RAG chatbot in Langchain powered by [OpenAI](https://platform.openai.com/overview). You can upload documents in txt, pdf, or docx formats and chat with your data. Relevant documents will be retrieved and sent to the LLM along with your follow-up questions for accurate answers.


![RAG Architecture](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/659f82867f92a9d5b24ad1f7_llamaindexlangchain.webp)  
(*Example architecture of a RAG model*)

## Installation <a name="installation"></a>

This project requires Python 3 and the langchain packages: `langchain` and `langchain-openai`.

## Instructions <a name="instructions"></a>

To run the app locally:

1. Create a virtual environment: `python -m venv my_first_rag_chatbot`
2. Activate the virtual environment : ` source my_first_rag_chatbot\bin\activate` 
3. Install the required dependencies: `pip install langchain langchain-openai `
4. Input your data in the ./data directory: Currently, the supported formats are txt, pdf, or docx files.
5. Step into our directory: `cd RAG_Chatbot`
6. Run the app: `python RAG_chatbot.py`



