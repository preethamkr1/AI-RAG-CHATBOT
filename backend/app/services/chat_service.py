from langchain_cohere import ChatCohere
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():

    llm = ChatCohere(
        model="command-a-03-2025",
        cohere_api_key=os.getenv(
            "COHERE_API_KEY"
        ),
        temperature=0.2,
        max_tokens=1024
    )

    return llm


def generate_answer(
    context,
    question
):

    llm = get_llm()

    prompt = f"""
You are an expert AI document analyst and retrieval assistant.

Your responsibilities:
- Answer questions using ONLY the provided context.
- Analyze information from multiple documents if required.
- Combine related information from different chunks.
- Explain your reasoning clearly.
- For comparison questions, compare values and identify trends.
- For analysis questions, provide observations and insights.
- For recommendation questions, provide suggestions supported by the document.
- Keep answers concise for direct factual questions.
- Provide detailed answers for analytical questions.

Guidelines:
1. Never invent information.
2. If multiple documents are involved, mention that information was gathered from multiple sources.
3. If numbers or scores are present, explain their significance when useful.
4. Prefer complete sentences instead of raw values.
5. If the answer is not present in the context, respond exactly with:
"I could not find this information in the uploaded documents."
6. If multiple sources support the answer, combine them into a single coherent response.
7. For comparisons, include tables or bullet points when useful.
8. Keep answers natural and easy to understand.

Document Context:
{context}

User Question:
{question}

Answer:
"""

    try:

        response = llm.invoke(
            prompt
        )

        if hasattr(response, "content"):
            return response.content

        return str(response)

    except Exception as e:

        print(
            f"\nCohere Error: {e}"
        )

        return (
            f"LLM Error: {str(e)}"
        )