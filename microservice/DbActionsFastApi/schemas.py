from pydantic import BaseModel

class AddBlog(BaseModel):
    header:str
    content:str


