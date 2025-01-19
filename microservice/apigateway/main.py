from fastapi import FastAPI
import httpx
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
Bloghome = "http://localhost:8001"
app.mount("/static", StaticFiles(directory="../BlogPageFlask"), name="static")

@app.get("/", response_class=HTMLResponse)
async def blogsPage():
    async with httpx.AsyncClient() as client:
        response= await client.get(f"{Bloghome}/")
        if(response.status_code != 200):
            return "Error"
        else:
            return response.text
