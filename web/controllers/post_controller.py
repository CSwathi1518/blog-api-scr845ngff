from flask import request
from web import db
from web.models.post import Post
from web.middleware.auth_middleware import get_current_user
from web.utils.validators import validate_post_data
from web.utils.helpers import success_response, error_response

def get_all_posts():
    """Get all posts"""
    try:
        posts = Post.query.order_by(Post.created_at.desc()).all()
        return success_response([post.to_dict() for post in posts])
    except Exception as e:
        return error_response(f'Failed to fetch posts: {str(e)}', status=500)

def get_post(post_id):
    """Get single post by ID"""
    try:
        post = Post.query.get(post_id)
        if not post:
            return error_response('Post not found', status=404)
        
        return success_response(post.to_dict())
    except Exception as e:
        return error_response(f'Failed to fetch post: {str(e)}', status=500)

def create_post():
    """Create a new post"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        data = request.get_json()
        
        # Validate input
        errors = validate_post_data(data)
        if errors:
            return error_response('Validation failed', errors, 400)
        
        # Create new post
        new_post = Post(
            title=data['title'],
            content=data['content'],
            author_id=current_user.id
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return success_response(
            new_post.to_dict(),
            'Post created successfully',
            201
        )
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to create post: {str(e)}', status=500)

def update_post(post_id):
    """Update a post"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        post = Post.query.get(post_id)
        if not post:
            return error_response('Post not found', status=404)
        
        # Check if user is the author
        if post.author_id != current_user.id:
            return error_response('You are not authorized to update this post', status=403)
        
        data = request.get_json()
        
        # Validate input
        errors = validate_post_data(data)
        if errors:
            return error_response('Validation failed', errors, 400)
        
        # Update post
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        
        db.session.commit()
        
        return success_response(post.to_dict(), 'Post updated successfully')
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to update post: {str(e)}', status=500)

def delete_post(post_id):
    """Delete a post"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        post = Post.query.get(post_id)
        if not post:
            return error_response('Post not found', status=404)
        
        # Check if user is the author
        if post.author_id != current_user.id:
            return error_response('You are not authorized to delete this post', status=403)
        
        db.session.delete(post)
        db.session.commit()
        
        return success_response(None, 'Post deleted successfully')
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to delete post: {str(e)}', status=500)