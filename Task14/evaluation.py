# Sample RAG responses

test_cases = [
    {
        "question": "What is RAG?",
        "expected": "Retrieval Augmented Generation combines retrieval with LLM generation.",
        "actual": "RAG combines document retrieval with an LLM to generate answers."
    },
    {
        "question": "What is LangChain?",
        "expected": "A framework for building LLM applications.",
        "actual": "LangChain is a framework for developing LLM-powered applications."
    },
    {
        "question": "Who is the Prime Minister of India?",
        "expected": "Not available in uploaded documents.",
        "actual": "I don't know because this information is not in the retrieved documents."
    }
]

def evaluate(expected, actual):
    expected = expected.lower()
    actual = actual.lower()

    if expected in actual or actual in expected:
        return 1

    common = len(set(expected.split()) & set(actual.split()))
    total = len(set(expected.split()))

    return round(common / total, 2)

print("="*60)

scores = []

for t in test_cases:
    score = evaluate(t["expected"], t["actual"])
    scores.append(score)

    print("Question :", t["question"])
    print("Score    :", score)
    print()

print("="*60)
print("Average Score:", round(sum(scores)/len(scores),2))