from fastapi import APIRouter,Depends
from schemas import addBlog,deleteBlog,getBlog,updateBlog
from repository.dbaccesRepo import Blog
from model import AddBlog 
from database import session
from sqlalchemy.orm import Session

router = APIRouter(tags=["Blogs"])
def dbaccess():
    db = session()
    try:
        yield db
    except Exception as e:
        db.close()
        raise e


@router.post("/new-blog",response_model=addBlog)
def addblogDef(schema:addBlog,db:Session=Depends(dbaccess)):
    blog_repo = Blog(db = db)
    return blog_repo.addBlog(model=Blog, schema=schema)

    
@router.delete("/delete-blog",response_model=deleteBlog)
def deleteBlogDef(blog:deleteBlog,db:Session=Depends(dbaccess)):
    blog_repo = Blog(db)
    return blog_repo.deleteBlog(model=AddBlog, schema=blog)

@router.put("/update-blog",response_model=updateBlog)
def updateBlogDef(blog:updateBlog,db:Session=Depends(dbaccess)):
    pass

@router.get("/get-blog-by-id",response_model=getBlog)
def get_post_by_id():
    pass

@router.get("/get-blogs",response_model=getBlog)
def get_posts():
    pass

