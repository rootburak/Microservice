from fastapi import Depends,HTTPException,status
from database import session
from schemas import addBlog,deleteBlog,getBlog,allBlogs,getById
from sqlalchemy.orm import Session
    

class RepoBlog():
    def __init__(self, db):
        self.db = db
    def addBlog(self,model,schema:addBlog):
        try:
            newBlog = model(header=schema.header,content=schema.content)
            self.db.add(newBlog)
            self.db.commit()
            return schema
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=error)


    def deleteBlog(self,id,model):
        try:
            blog = self.db.query(model).filter(model.id == id).first()
            if blog:
                self.db.delete(blog)
                self.db.commit()
                return blog
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    def updateBlog(self,model,schema,id):
        try:
            blog = self.db.query(model).filter(model.id ==id).first()
            if blog:
                blog.header = schema.header
                blog.content = schema.content
                self.db.commit()
                return schema
            else:
                return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    def allBlogs(self,model):
        try:
            blog = self.db.query(model).all()
            return blog
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=error)
    def getBlog(self,model,id):
        try:
            print(id)
            blog = self.db.query(model).filter(model.id==id).first()
            return blog
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=error)


