from fastapi import APIRouter,Depends
from schemas import allBlogs,addBlog,deleteBlog,getBlog,getById
from repository.dbaccesRepo import RepoBlog
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
    blog_repo = RepoBlog(db = db)
    return blog_repo.addBlog(model=AddBlog, schema=schema)

    
@router.delete("/delete-blog/{id}")
def deleteBlogDef(id,db:Session=Depends(dbaccess)):
    blog_repo = RepoBlog(db)
    return blog_repo.deleteBlog(model=AddBlog,id=id)

@router.put("/update-blog/{id}")
def updateBlogDef(id,blog:addBlog,db:Session=Depends(dbaccess)):
    blog_repo = RepoBlog(db)
    return blog_repo.updateBlog(model=AddBlog,schema=blog,id=id)

@router.get("/get-blog-by-id/{id}")
def get_post_by_id(id,db:Session=Depends(dbaccess)):
    blog_repo=RepoBlog(db)
    return blog_repo.getBlog(model=AddBlog,id=id)
@router.get("/get-blogs")
def getAllBlogs(db:Session=Depends(dbaccess)):
    blog_repo=RepoBlog(db) 
    return blog_repo.allBlogs(model=AddBlog) 

