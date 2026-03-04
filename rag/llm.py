from langchain_ollama import OllamaLLM


def generate_answer(context, question):

    llm = OllamaLLM(model="llama3")

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response