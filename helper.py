from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


def document_loader(file_path):
    if (not file_path.endswith(".csv")):
        raise ValueError("File must be a CSV file.")
    with open(file_path, "r") as f:
        header = f.readline()
        if not header:
            raise ValueError("File must contain a header.")
        if "prompt" not in header or "response" not in header:
            raise ValueError("Your file doesn't contain the required columns.")

    loader = CSVLoader(
        file_path=file_path,
        source_column="prompt",
    )
    data = loader.load()
    return data


def getAnswerFromLLM(data, query):

    load_dotenv()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        temperature=0.5,
        max_output_tokens=256,
        top_p=0.95,
        top_k=40,
        stop=["\n\n"],
        google_api_key=os.environ["GOOGLE_API_KEY"]
    )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", google_api_key=os.environ["GOOGLE_API_KEY"])

    vectorstore = FAISS.from_documents(data, embeddings)
    retriever = vectorstore.as_retriever()

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    result = chain.invoke({"input": query})
    return result['answer']
