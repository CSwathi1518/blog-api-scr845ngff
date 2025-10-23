from flask import request
from web import db
from web.models.comment import Comment
from web.models.post import Post
from web.middleware.auth_middleware import get_current_user
from web.utils.validators import validate_comment_data
from web.utils.helpers import success_response, error_response

def get_comments():
    """Get comments for a post"""
    try:
        post_id = request.args.get('post_id')
        
        if not post_id:
            return error_response('post_id parameter is required', status=400)
        
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
        return success_response([comment.to_dict() for comment in comments])
        
    except Exception as e:
        return error_response(f'Failed to fetch comments: {str(e)}', status=500)

def get_comment(comment_id):
    """Get single comment by ID"""
    try:
        comment = Comment.query.get(comment_id)
        if not comment:
            return error_response('Comment not found', status=404)
        
        return success_response(comment.to_dict())
    except Exception as e:
        return error_response(f'Failed to fetch comment: {str(e)}', status=500)

def create_comment():
    """Create a new comment"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        data = request.get_json()
        
        # Validate input
        errors = validate_comment_data(data)
        if errors:
            return error_response('Validation failed', errors, 400)
        
        # Check if post exists
        post = Post.query.get(data['post_id'])
        if not post:
            return error_response('Post not found', status=404)
        
        # Create new comment
        new_comment = Comment(
            content=data['content'],
            post_id=data['post_id'],
            author_id=current_user.id
        )
        
        db.session.add(new_comment)
        db.session.commit()
        
        return success_response(
            new_comment.to_dict(),
            'Comment created successfully',
            201
        )
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to create comment: {str(e)}', status=500)

def update_comment(comment_id):
    """Update a comment"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        comment = Comment.query.get(comment_id)
        if not comment:
            return error_response('Comment not found', status=404)
        
        # Check if user is the author
        if comment.author_id != current_user.id:
            return error_response('You are not authorized to update this comment', status=403)
        
        data = request.get_json()
        
        if not data.get('content'):
            return error_response('Content is required', status=400)
        
        # Update comment
        comment.content = data['content']
        
        db.session.commit()
        
        return success_response(comment.to_dict(), 'Comment updated successfully')
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to update comment: {str(e)}', status=500)

def delete_comment(comment_id):
    """Delete a comment"""
    try:
        current_user = get_current_user()
        if not current_user:
            return error_response('Authentication required', status=401)
        
        comment = Comment.query.get(comment_id)
        if not comment:
            return error_response('Comment not found', status=404)
        
        # Check if user is the author
        if comment.author_id != current_user.id:
            return error_response('You are not authorized to delete this comment', status=403)
        
        db.session.delete(comment)
        db.session.commit()
        
        return success_response(None, 'Comment deleted successfully')
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Failed to delete comment: {str(e)}', status=500)