from pydantic import BaseModel

class addBlog(BaseModel):
    header:str
    content:str
    class Config:
        orm_mode = True
class deleteBlog(BaseModel):
    id:int
    class Config:
        orm_mode = True

class getBlog(BaseModel):
    id:int
    header:str
    content:str
    class Config:
        orm_mode = True
class allBlogs(BaseModel):
    header:str
    content:str
class getById(BaseModel):
    id:int
