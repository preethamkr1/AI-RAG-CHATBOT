from fastapi import APIRouter, Depends

from app.models.chat_model import ChatRequest
from app.services.vector_service import get_retriever
from app.services.chat_service import generate_answer
from app.services.bm25_service import search_bm25
from app.services.rerank_service import rerank_documents
from app.services.query_expansion_service import expand_query
from app.services.memory_service import (
    get_chat_history,
    add_to_chat_history
)
from app.services.dependency_service import (
    get_current_user
)

router = APIRouter()


@router.post("/ask")
async def ask_question(
    request: ChatRequest,
    user_id: str = Depends(
        get_current_user
    )
):

    session_id = (
        f"{user_id}_{request.session_id}"
    )

    # ================= MULTIPLE QUESTIONS =================
    if request.questions:

        results = []

        for question in request.questions:

            expanded_question = expand_query(
                question
            )

            print(
                f"\nUser: {user_id}"
            )
            print(
                f"Original Query: {question}"
            )
            print(
                f"Expanded Query: "
                f"{expanded_question}"
            )

            # ---------- HISTORY ----------
            history = get_chat_history(
                session_id
            )

            history_text = ""

            for item in history:
                history_text += (
                    f"User: "
                    f"{item['question']}\n"
                    f"Assistant: "
                    f"{item['answer']}\n\n"
                )

            # ---------- FAISS SEARCH ----------
            retriever = get_retriever(
                user_id=user_id
            )

            vector_docs = retriever.invoke(
                expanded_question
            )

            # ---------- BM25 SEARCH ----------
            bm25_chunks = search_bm25(
                expanded_question,
                top_k=10
            )

            # ---------- MERGE ----------
            all_documents = []

            for doc in vector_docs:
                all_documents.append(
                    doc.page_content
                )

            all_documents.extend(
                bm25_chunks
            )

            all_documents = list(
                dict.fromkeys(
                    all_documents
                )
            )

            print(
                f"\nRetrieved before "
                f"reranking: "
                f"{len(all_documents)}"
            )

            # ---------- RERANK ----------
            reranked_documents = (
                rerank_documents(
                    expanded_question,
                    all_documents,
                    top_n=5
                )
            )

            print(
                f"Retrieved after "
                f"reranking: "
                f"{len(reranked_documents)}"
            )

            # ---------- CONTEXT ----------
            document_context = (
                "\n\n".join(
                    reranked_documents
                )
            )

            full_context = f"""
Conversation History:
{history_text}

Document Context:
{document_context}
"""

            answer = generate_answer(
                full_context,
                question
            )

            # ---------- MEMORY ----------
            add_to_chat_history(
                session_id,
                question,
                answer
            )

            # ---------- SOURCES ----------
            source_documents = list(
                set(
                    [
                        doc.metadata.get(
                            "source",
                            "Unknown"
                        )
                        for doc in vector_docs
                    ]
                )
            )

            results.append(
                {
                    "question":
                        question,
                    "answer":
                        answer,
                    "sources":
                        source_documents
                }
            )

        return {
            "user_id":
                user_id,
            "session_id":
                request.session_id,
            "results":
                results,
            "conversation_history_size":
                len(
                    get_chat_history(
                        session_id
                    )
                )
        }

    # ================= SINGLE QUESTION =================

    question = request.question

    expanded_question = (
        expand_query(
            question
        )
    )

    print(
        f"\nUser: {user_id}"
    )
    print(
        f"Original Query: "
        f"{question}"
    )
    print(
        f"Expanded Query: "
        f"{expanded_question}"
    )

    # ---------- HISTORY ----------
    history = get_chat_history(
        session_id
    )

    history_text = ""

    for item in history:
        history_text += (
            f"User: "
            f"{item['question']}\n"
            f"Assistant: "
            f"{item['answer']}\n\n"
        )

    # ---------- FAISS SEARCH ----------
    retriever = get_retriever(
        user_id=user_id
    )

    vector_docs = retriever.invoke(
        expanded_question
    )

    # ---------- BM25 SEARCH ----------
    bm25_chunks = search_bm25(
        expanded_question,
        top_k=10
    )

    # ---------- MERGE ----------
    all_documents = []

    for doc in vector_docs:
        all_documents.append(
            doc.page_content
        )

    all_documents.extend(
        bm25_chunks
    )

    all_documents = list(
        dict.fromkeys(
            all_documents
        )
    )

    print(
        f"\nRetrieved before "
        f"reranking: "
        f"{len(all_documents)}"
    )

    # ---------- RERANK ----------
    reranked_documents = (
        rerank_documents(
            expanded_question,
            all_documents,
            top_n=5
        )
    )

    print(
        f"Retrieved after "
        f"reranking: "
        f"{len(reranked_documents)}"
    )

    # ---------- CONTEXT ----------
    document_context = (
        "\n\n".join(
            reranked_documents
        )
    )

    full_context = f"""
Conversation History:
{history_text}

Document Context:
{document_context}
"""

    answer = generate_answer(
        full_context,
        question
    )

    # ---------- MEMORY ----------
    add_to_chat_history(
        session_id,
        question,
        answer
    )

    # ---------- SOURCES ----------
    source_documents = list(
        set(
            [
                doc.metadata.get(
                    "source",
                    "Unknown"
                )
                for doc in vector_docs
            ]
        )
    )

    return {
        "user_id":
            user_id,
        "session_id":
            request.session_id,
        "question":
            question,
        "expanded_question":
            expanded_question,
        "answer":
            answer,
        "sources":
            source_documents,
        "conversation_history_size":
            len(
                get_chat_history(
                    session_id
                )
            )
    }