from fastapi import FastAPI
from database import engine,base
from router import chat
import models 

models.base.metadata.create_all(bind = engine)


app = FastAPI(title="Ai-Agent")

app.include_router(chat.router)

