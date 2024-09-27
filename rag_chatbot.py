from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

class RAGChatbot:
    def __init__(self, file_path, api_key):
        self.file_path = file_path
        self.api_key = api_key
        self.docs = None
        self.retriever = None
        self.qa = None

        # Set API key for OpenAI
        self.set_openai_api_key(api_key)

        # Load and split the documents
        self.load_and_split_documents()

        # Initialize the vector store and retriever
        self.initialize_retriever()

        # Initialize the chat model
        self.initialize_chatbot()

    def set_openai_api_key(self, api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        print("OpenAI API Key has been set.")

    def load_document(self):
        if self.file_path.endswith('.pdf'):
            loader = PyPDFLoader(self.file_path)
            documents = loader.load()
            print(f"Loaded {len(documents)} pages from PDF.")
        elif self.file_path.endswith('.txt'):
            loader = TextLoader(self.file_path, encoding='utf-8')
            documents = loader.load()
            print(f"Loaded {len(documents)} documents from text file.")
        else:
            raise ValueError("Unsupported file format. Please use .pdf, .txt")
        return documents

    def load_and_split_documents(self):
        documents = self.load_document()

        # Split the document into chunks
        r_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=150,
            separators=["\n\n", "\n", "(?<=\. )", " ", ""]
        )
        self.docs = r_splitter.split_documents(documents)
        print(f"Number of documents after splitting: {len(self.docs)}")

    def initialize_retriever(self):
        # Embedding the documents into vector representations
        embedding = OpenAIEmbeddings()

        # Vector store for holding all the vectors
        vectordb = Chroma.from_documents(
            documents=self.docs,
            embedding=embedding
        )

        # Set up retriever
        self.retriever = vectordb.as_retriever()
        print("Retriever has been initialized.")

    def initialize_chatbot(self):
        # Initialize LLM
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        # Memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Conversational Retrieval Chain
        self.qa = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=self.retriever,
            memory=memory
        )
        print("Chatbot has been initialized.")

    def chat(self):
        print("Welcome to the chatbot! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            response = self.qa.invoke(input=user_input)
            print(f"Bot: {response['answer']}")


if __name__ == "__main__":
    file_path = input("Please enter the file path (.pdf or .txt): ")
    api_key = input("Please enter your OpenAI API key: ")

    chatbot = RAGChatbot(file_path, api_key)
    chatbot.chat()
