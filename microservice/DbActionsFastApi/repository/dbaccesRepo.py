from fastapi import Depends,HTTPException,status
from ..database import session
from ..schemas import AddBlog,DeleteBlog,UpdateBlog
from sqlalchemy import Session
    
def dbaccess():
    db = session()
    try:
        yield db
    except:
        db.close()


def addBlog(model,schema:AddBlog, db:Session = Depends(dbaccess)):
    try:
        newBlog = model(header=schema.header,content=schema.content)
        db.save(newBlog)
        db.commit()
    except Exception as e:
        db.rollback()
        error = e.args[0]
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=error)


def deleteBlog(model,schema:DeleteBlog, db:Session = Depends(dbaccess)):
    try:
        blog = db.query(model).filter(model.id == schema.id).first()
        if blog:
            db.delete(blog)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    except Exception as e:
        db.rollback()
        error = e.args[0]
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def updateBlog(model,schema:UpdateBlog, db:Session = Depends(dbaccess)):
    try:
        blog = db.query(model).filter(model.id == schema.id).first()
        if blog:
            blog.header = schema.header
            blog.content = schema.content
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    except Exception as e:
        db.rollback()
        error = e.args[0]
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)





