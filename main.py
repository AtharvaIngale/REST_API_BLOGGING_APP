from fastapi import FastAPI, Body
from models import BlogPost, Comment, Like
from database import (
    get_blog_posts,
    create_blog_post,
    get_comments,
    create_comment,
    delete_comment,
    get_likes,
    create_like,
    delete_like,
)

app = FastAPI()

@app.get("/posts")
async def get_all_posts():
    return await get_blog_posts()

@app.post("/posts")
async def create_post(post: BlogPost = Body(...)):
    await create_blog_post(post)
    return {"message": "Your post is live!"}

@app.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int):
    return await get_comments(post_id)

@app.post("/posts/{post_id}/comments")
async def create_post_comment(comment: Comment, post_id: int):
    await create_comment(comment, post_id)
    return {"message": "Comment added successfully"}

@app.delete("/comments/{comment_id}")
async def delete_a_comment(comment_id: int):
    await delete_comment(comment_id)
    return {"message": "Comment deleted successfully"}

@app.get("/posts/{post_id}/likes")
async def get_post_likes(post_id: int):
    return await get_likes(post_id)

@app.post("/posts/{post_id}/likes")
async def like_a_post(like: Like = Body(...), post_id: int):
    # Check if user already liked the post
    existing_like = await db.likes.find_one({"user_id": like.user_id, "post_id": post_id})
    if existing_like:
        return {"message": "User already liked this post"}

    await create_like(like, post_id)
    return {"message": "Post liked successfully"}
