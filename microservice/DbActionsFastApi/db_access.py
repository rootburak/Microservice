from fastapi import FastAPI,APIRouter
from database import save_db


save_db()
app = FastAPI()

APIRouter()
