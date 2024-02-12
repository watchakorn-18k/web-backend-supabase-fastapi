from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Course(BaseModel):
    id: Optional[int] = 0
    name: Optional[str]
    created_at: Optional[str] = Field(default=datetime.now().isoformat())
    price: Optional[int]
    details: Optional[str] = Field(default=None)
    uid: Optional[str]
