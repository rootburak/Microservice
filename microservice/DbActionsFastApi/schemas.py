from pydantic import BaseModel

class AddBlog(BaseModel):
    header:str
    content:str
class DeleteBlog(BaseModel):
    id:int

class UpdateBlog(BaseModel):
    id:int
    header:str
    content:str
class GetBlog(BaseModel):
    id:int
    header:str
    content:str

