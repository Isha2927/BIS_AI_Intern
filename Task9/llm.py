from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)

# LLM
llm = ChatGroq(
    groq_api_key="API KEY",
    model_name="llama-3.1-8b-instant"
)

# Output Parser
parser = StrOutputParser()

# Create Chain
chain = prompt | llm | parser

# Invoke Chain
response = chain.invoke({"topic": "Artificial Intelligence"})

print(response)