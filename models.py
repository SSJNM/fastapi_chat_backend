from sqlalchemy import Boolean,Column,Integer, String,VARCHAR
from database import Base


class Chat(Base):
    __tablename__ = "chat_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(length=255), index=True)
    message = Column(VARCHAR(length=255),index=True)
    is_active = Column(Boolean, default=True)
