from pymongo import MongoClient
from bson import ObjectId

from app.services.password_service import (
    hash_password,
    verify_password
)

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["rag_chatbot"]

users_collection = db["users"]


def register_user(
    name,
    email,
    password
):

    existing_user = users_collection.find_one(
        {
            "email": email
        }
    )

    if existing_user:
        return None

    result = users_collection.insert_one(
        {
            "name": name,
            "email": email,
            "password": hash_password(
                password
            )
        }
    )

    return str(
        result.inserted_id
    )


def authenticate_user(
    email,
    password
):

    user = users_collection.find_one(
        {
            "email": email
        }
    )

    if not user:
        return None

    if not verify_password(
        password,
        user["password"]
    ):
        return None

    return str(
        user["_id"]
    )


def get_user_by_id(
    user_id
):

    user = users_collection.find_one(
        {
            "_id": ObjectId(
                user_id
            )
        }
    )

    if not user:
        return None

    return {
        "id": str(
            user["_id"]
        ),
        "name": user["name"],
        "email": user["email"]
    }