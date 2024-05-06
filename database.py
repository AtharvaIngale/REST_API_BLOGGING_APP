from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["blog_db"]  #database name

async def get_blog_posts():
    posts = db.posts.find()
    return list(posts)

async def create_blog_post(post: BlogPost):
    db.posts.insert_one(post.dict())

async def get_comments(post_id: int):
    comments = db.comments.find({"post_id": post_id})
    return list(comments)

async def create_comment(comment: Comment, post_id: int):
    comment.update({"post_id": post_id})
    db.comments.insert_one(comment.dict())

async def delete_comment(comment_id: int):
    db.comments.delete_one({"_id": comment_id})

async def get_likes(post_id: int):
    likes = db.likes.find({"post_id": post_id})
    return list(likes)

async def create_like(like: Like, post_id: int):
    like.update({"post_id": post_id})
    db.likes.insert_one(like.dict())

async def delete_like(like_id: int):
    db.likes.delete_one({"_id": like_id})
