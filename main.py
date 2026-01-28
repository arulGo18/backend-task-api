from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import user, task

app = FastAPI(title="Task API Dengan User")

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(task.router)
