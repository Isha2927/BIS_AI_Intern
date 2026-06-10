from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from groq import Groq


pdf_path = "the_aadhaar_act_2016.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print("PDF Loaded Successfully!")
print("Total Pages:", len(documents))



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

print("Total Chunks Created:", len(docs))


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

print("FAISS Vector Database Created!")


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)



client = Groq(
    api_key="Github does not allow sharing of secrets, so I have removed the API key from the code snippet. "
)


while True:

    question = input("\nAsk a Question (type exit to quit): ")

    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    retrieved_docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    print("\n========== RETRIEVED CONTEXT ==========\n")
    print(context[:2000])
    print("\n=======================================\n")

    prompt = f"""
You are a question-answering assistant.

Answer ONLY using the provided context.

The wording of the question does not need to exactly match
the wording in the document.

If the context contains information relevant to the question,
answer it clearly.

Only respond:
"The information is not available in the document."

when the context does not contain enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    print("\n========== ANSWER ==========\n")
    print(answer)

    print("\n========== SOURCE CHUNKS ==========\n")

    for i, doc in enumerate(retrieved_docs, start=1):

        page = doc.metadata.get("page", "Unknown")

        print(f"\nChunk {i} | Page {page + 1}")
        print("-" * 60)
        print(doc.page_content[:400])

    print("\n" + "=" * 70)