from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import models, schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def start():
    return {"key": "value"}

@app.post('/post-data')
async def postdata(data:dict):
    return data

@app.post("/post-chat/", response_model=schemas.Chat)
def create_chat(chat: schemas.ChatBase, db: Session = Depends(get_db)):
    # name=chat.name
    # db_chat = db.query(models.Chat).filter(models.Chat.name == name).first()
    # if db_chat:
    #     raise HTTPException(status_code=400, detail="Message already printed")
    db_chat = models.Chat(name=chat.name, message=chat.message)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


@app.get("/chats/", response_model=List[schemas.Chat])
def read_chat(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.Chat).offset(skip).limit(limit).all()
    return users