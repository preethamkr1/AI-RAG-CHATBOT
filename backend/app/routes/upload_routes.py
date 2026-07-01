from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from app.services.pdf_service import (
    extract_text_from_pdf
)

from app.services.chunk_service import (
    create_chunks
)

from app.services.embedding_service import (
    get_embedding_model
)

from app.services.vector_service import (
    create_vector_store
)

from app.services.dependency_service import (
    get_current_user
)

import shutil
import os

router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    user_id: str = Depends(
        get_current_user
    )
):

    # Create user upload folder
    user_upload_folder = (
        f"uploads/{user_id}"
    )

    os.makedirs(
        user_upload_folder,
        exist_ok=True
    )

    # Save PDF inside user folder
    upload_path = (
        f"{user_upload_folder}/{file.filename}"
    )

    with open(
        upload_path,
        "wb"
    ) as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    print(
        f"\nPDF saved for user "
        f"{user_id}"
    )

    # Extract text
    text = extract_text_from_pdf(
        upload_path
    )

    # Create chunks
    chunks = create_chunks(
        text
    )

    # Metadata for every chunk
    metadata = []

    for index, chunk in enumerate(
        chunks
    ):
        metadata.append(
            {
                "user_id": user_id,
                "source": file.filename,
                "chunk_number": (
                    index + 1
                )
            }
        )

    print(
        f"\nMetadata created "
        f"for {len(metadata)} chunks."
    )

    # Embedding model
    embeddings = (
        get_embedding_model()
    )

    # Create user-specific FAISS
    vector_store = (
        create_vector_store(
            chunks=chunks,
            embeddings=embeddings,
            metadata=metadata,
            user_id=user_id
        )
    )

    print(
        "\nUser Vector Store "
        "Created Successfully."
    )

    return {
        "message":
            "PDF uploaded successfully",
        "user_id": user_id,
        "filename": file.filename,
        "total_chunks": len(chunks),
        "vector_database_created": True
    }