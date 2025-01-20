from sqlalchemy import Column,String,Integer
from database import Base
class AddBlog(Base):
    __tablename__="blogs"
    id = Column(Integer, primary_key=True)
    header = Column(String(100))
    content = Column(String(500))
    def __init__(self,header,content):
        self.header = header
        self.content = content
    def __repr__(self):
        return f'<Blog(id={self.id}, header="{self.header}", content="{self.content}")>'
