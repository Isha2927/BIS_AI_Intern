from rag import retrieve

def answer_question(question):

    contexts = retrieve(question)

    answer = "\n".join(contexts)

    return answer


while True:

    question = input("\nAsk a medical question (type exit to quit): ")

    if question.lower() == "exit":
        break

    answer = answer_question(question)

    print("\n===== ANSWER =====\n")
    print(answer)