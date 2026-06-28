from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser


pdf_path = "the_aadhaar_act_2016.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print("PDF Loaded Successfully!")
print(f"Total Pages: {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)

print(f"Total Chunks: {len(docs)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)

print("FAISS Vector Store Ready!")


llm = ChatGroq(
    groq_api_key="YOUR_GROQ_API_KEY",
    model_name="llama-3.1-8b-instant"
)

memory = ConversationBufferMemory(
    return_messages=True
)

prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Use ONLY the provided document context to answer.

Conversation History:
{history}

Context:
{context}

Question:
{question}

If the answer is not present in the context, reply:

"The information is not available in the document."

Answer:
"""
)

parser = StrOutputParser()

print("\n===== RAG Chatbot Started =====")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    # Retrieve documents
    retrieved_docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # Memory
    history = memory.load_memory_variables({})["history"]

    # Prompt
    formatted_prompt = prompt.format(
        history=history,
        context=context,
        question=question
    )

    # LLM
    response = llm.invoke(formatted_prompt)

    answer = parser.invoke(response)

    # Save Memory
    memory.save_context(
        {"input":question},
        {"output":answer}
    )

    # Print Answer
    print("\nBot:")
    print(answer)

    # Source Citations
    print("\nSources:")

    for i, doc in enumerate(retrieved_docs, start=1):

        page = doc.metadata.get("page", "Unknown")

        print(f"Page {page+1}")

    print("-"*60)