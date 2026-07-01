from pydantic import BaseModel
from typing import Optional, List


class ChatRequest(BaseModel):
    question: Optional[str] = None
    questions: Optional[List[str]] = None
    session_id: str = "default"