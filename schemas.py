from typing import List, Union
from pydantic import BaseModel


class ChatBase(BaseModel):
    name: str
    message: str

class Chat(ChatBase):
    id: int
    is_active: bool

    class Config:
        # orm_mode = True depriciated
        from_attributes = True