# Blog API - SCR845NGFF

A RESTful API for a blog application with user authentication, posts, and comments.

## Setup Instructions

1. Create virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```

2. Install dependencies:
```
   pip install -r requirements.txt
```

3. Set up environment variables in `.env`

4. Initialize database:
```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
```

5. Run the application:
```
   python run.py
```

## API Endpoints

- POST /api/auth/register - Register new user
- POST /api/auth/login - Login user
- GET /api/posts - Get all posts
- POST /api/posts - Create new post
- GET /api/posts/{id} - Get single post
- PUT /api/posts/{id} - Update post
- DELETE /api/posts/{id} - Delete post
- POST /api/comments - Create comment
- GET /api/comments?post_id={id} - Get comments for a post
- PUT /api/comments/{id} - Update comment
- DELETE /api/comments/{id} - Delete comment