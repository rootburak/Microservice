from fastapi import FastAPI,APIRouter
from database import save_db
from route.dbaccess import router as dbroute

save_db()
app = FastAPI()

app.include_router(dbroute)
