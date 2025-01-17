from fastapi import APIRouter
from ..schemas import AddBlog

router = APIRouter(tags=["Blogs"])

router.post("/new-post",response_model=AddBlog)
def new_post(response_model=AddBlog):
    pass
router.get("get-post-by-id",response_model=AddBlog)
def get_post_by_id():
    pass
