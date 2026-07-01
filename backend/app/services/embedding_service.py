from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def get_embedding_model():
    embeddings = CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )

    return embeddings