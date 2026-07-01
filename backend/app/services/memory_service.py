from pymongo import MongoClient
from datetime import datetime

# MongoDB Connection
client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["rag_chatbot"]

chat_collection = db["chat_history"]


def get_chat_history(
    session_id: str
):

    conversations = (
        chat_collection.find(
            {
                "session_id": session_id
            }
        )
        .sort(
            "created_at",
            1
        )
    )

    history = []

    for item in conversations:

        history.append(
            {
                "question": item["question"],
                "answer": item["answer"]
            }
        )

    return history


def add_to_chat_history(
    session_id: str,
    question: str,
    answer: str
):

    chat_collection.insert_one(
        {
            "session_id": session_id,
            "question": question,
            "answer": answer,
            "created_at": datetime.utcnow()
        }
    )

    # Keep only latest 10 conversations
    total_conversations = list(
        chat_collection.find(
            {
                "session_id": session_id
            }
        ).sort(
            "created_at",
            1
        )
    )

    if len(total_conversations) > 10:

        old_messages = (
            total_conversations[:-10]
        )

        for message in old_messages:

            chat_collection.delete_one(
                {
                    "_id": message["_id"]
                }
            )