# Task 12 - Simple Agentic AI System

knowledge = {
    "rag": "Retrieval-Augmented Generation combines document retrieval with LLM generation.",
    "langgraph": "LangGraph is a framework for building stateful AI agents using graph-based workflows.",
    "crewai": "CrewAI is a framework for building multi-agent systems where agents collaborate using assigned roles.",
    "llm": "A Large Language Model generates human-like text based on input prompts."
}

def calculator(expression):
    return eval(expression)

def knowledge_tool(topic):
    return knowledge.get(topic.lower(), "No information available.")

def agent(task):
    print("=" * 50)
    print("Task:", task)

    print("\nStep 1: Reasoning")
    if any(op in task for op in ["+", "-", "*", "/"]):
        print("Decision: Use Calculator Tool")
        result = calculator(task)

    else:
        print("Decision: Use Knowledge Tool")
        result = knowledge_tool(task)

    print("\nStep 2: Observation")
    print(result)

    print("\nStep 3: Final Answer")
    print(result)

print("Simple Agentic AI")

agent("RAG")
agent("LangGraph")
agent("20+35")
agent("CrewAI")