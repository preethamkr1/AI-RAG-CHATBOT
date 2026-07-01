import os

from langchain_community.vectorstores import FAISS
from app.services.embedding_service import get_embedding_model

# Cache loaded vector stores
_vector_stores = {}


def create_vector_store(
    chunks,
    embeddings,
    metadata=None,
    user_id=None
):
    global _vector_stores

    if user_id is None:
        raise Exception("user_id is required")

    # User specific vector path
    vector_path = f"vector_store/{user_id}"

    os.makedirs(
        vector_path,
        exist_ok=True
    )

    # Empty metadata if not provided
    if metadata is None:
        metadata = [{} for _ in chunks]

    # Existing user vector database
    if os.path.exists(
        f"{vector_path}/index.faiss"
    ):

        print(
            f"\nLoading existing vector database "
            f"for user {user_id}..."
        )

        vector_store = FAISS.load_local(
            vector_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

        print(
            "\nAdding new chunks..."
        )

        vector_store.add_texts(
            texts=chunks,
            metadatas=metadata
        )

    # First upload for user
    else:

        print(
            f"\nCreating new vector database "
            f"for user {user_id}..."
        )

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings,
            metadatas=metadata
        )

    # Save user vector database
    vector_store.save_local(
        vector_path
    )

    # Cache in RAM
    _vector_stores[user_id] = vector_store

    return vector_store


def load_vector_store(
    user_id
):
    global _vector_stores

    # Already loaded
    if user_id in _vector_stores:
        return _vector_stores[user_id]

    vector_path = (
        f"vector_store/{user_id}"
    )

    if not os.path.exists(
        f"{vector_path}/index.faiss"
    ):
        raise Exception(
            "No documents uploaded for this user."
        )

    embeddings = (
        get_embedding_model()
    )

    vector_store = FAISS.load_local(
        vector_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    _vector_stores[user_id] = (
        vector_store
    )

    return vector_store


def get_retriever(
    user_id,
    search_type="mmr",
    k=15,
    fetch_k=40
):

    vector_store = (
        load_vector_store(
            user_id
        )
    )

    retriever = (
        vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={
                "k": k,
                "fetch_k": fetch_k
            }
        )
    )

    return retriever