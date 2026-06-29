from langfuse import Langfuse

langfuse = Langfuse()

trace = langfuse.trace(name="RAG Demo")

retrieval = trace.span(name="Retrieve")

context = open("knowledge.txt").read()

retrieval.end(output=context)

generation = trace.generation(
    name="Answer",
    model="gpt-4o-mini",
    input=context + question
)

response = client.responses.create(
    model="gpt-4o-mini",
    input=f"Context:\n{context}\n\nQuestion:{question}"
)

answer = response.output_text

generation.end(output=answer)

trace.score(
    name="quality",
    value=1
)

print(answer)