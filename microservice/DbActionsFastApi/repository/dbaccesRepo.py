from fastapi import Depends,HTTPException,status
from database import session
from schemas import addBlog,deleteBlog,updateBlog,getBlog
from sqlalchemy.orm import Session
    

class Blog():
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


    def deleteBlog(self,model,schema:deleteBlog):
        try:
            blog = self.db.query(model).filter(model.id == schema.id).first()
            if blog:
                self.db.delete(blog)
                self.db.commit()
                return schema
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
        except Exception as e:
            self.db.rollback()
            error = e.args[0]
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    def updateBlog(self,model,schema:updateBlog):
        try:
            blog = self.db.query(model).filter(model.id == schema.id).first()
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





