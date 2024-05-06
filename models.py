from pydantic import BaseModel, Field

class Comment(BaseModel):
    content: str = Field(..., min_length=10)
    author: str

class Like(BaseModel):
    user_id: int

class BlogPost(BaseModel):
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=20)
    comments: List[Comment] = []
    likes: List[Like] = []
