import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(
    os.getenv("COHERE_API_KEY")
)


def rerank_documents(
    question,
    documents,
    top_n=5
):

    if len(documents) <= top_n:
        return documents

    results = co.rerank(
        query=question,
        documents=documents,
        top_n=top_n,
        model="rerank-v3.5"
    )

    reranked_docs = []

    for result in results.results:
        reranked_docs.append(
            documents[result.index]
        )

    return reranked_docs