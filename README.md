## Blogging Platform Using REST API

This API provides a RESTful interface for a simple blogging platform built with Python's FASTAPI framework and utilizes MongoDB for data storage. It adheres to object-oriented programming principles and allows users to:

* Create, Read, Update, and Delete (CRUD) blog posts.
* Add comments to posts.
* Like and dislike posts.

### Getting Started

**Prerequisites:**

* Python 3.6+
* uvicorn (ASGI server)
* pymongo (MongoDB driver)
* fastapi (web framework)
* pydantic (data validation)

**Installation:**

```bash
pip install uvicorn pymongo fastapi pydantic
```

**Project Structure:**

* `main.py`: Main application file with API definition.
* `models.py`: Data models for blog posts, comments, etc.
* `database.py`: Handles connecting and interacting with MongoDB.

**Running the API:**

1. Clone this repository (if applicable) or create a project directory.
2. Create the above-mentioned files within the project directory.
3. Replace `"mongodb://localhost:27017/"` in `database.py` with your actual MongoDB connection string.
4. Open a terminal in the project directory.
5. Start the application using uvicorn:

```bash
uvicorn main:app
```

### API Endpoints

**Blog Posts:**

* **GET /posts:** Retrieves all blog posts.
* **POST /posts:** Creates a new blog post. (Body: BlogPost model)
* (Optional) Implement functionalities for updating and deleting blog posts.

**Comments:**

* **GET /posts/{post_id}/comments:** Retrieves all comments for a specific post. (Path: post_id)
* **POST /posts/{post_id}/comments:** Creates a new comment for a specific post. (Body: Comment model, Path: post_id)
* **DELETE /comments/{comment_id}:** Deletes a comment. (Path: comment_id)

**Likes:**

* **GET /posts/{post_id}/likes:** Retrieves all likes for a specific post. (Path: post_id)
* **POST /posts/{post_id}/likes:** Creates a like for a specific post. (Body: Like model, Path: post_id)
* (Optional) Implement functionality for deleting a like.

**Data Models:**

The API utilizes Pydantic models to define the structure and validation rules for data:

* `models.py` contains definitions for `User` (optional for future features), `Comment`, `Like`, and `BlogPost` models.

