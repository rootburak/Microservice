from fastapi import APIRouter
from ..schemas import AddBlog,DeleteBlog,GetBlog,UpdateBlog

router = APIRouter(tags=["Blogs"])

router.post("/new-blog",response_model=AddBlog)
def new_post():
    pass
router.delete("/delete-blog",response_model=DeleteBlog)

router.put("/update-blog",response_model=UpdateBlog)

router.get("/get-blog-by-id",response_model=GetBlog)
def get_post_by_id():
    pass
router.get("/get-blogs",response_model=GetBlog)
def get_posts():
    pass

