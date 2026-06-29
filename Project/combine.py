from rag import retrieve

question = "What does high lactate mean?"

results = retrieve(question)

for r in results:
    print("\n")
    print(r)