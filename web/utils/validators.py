import re
from email_validator import validate_email, EmailNotValidError

def validate_user_registration(data):
    """Validate user registration data"""
    errors = []
    
    # Check required fields
    if not data.get('username'):
        errors.append('Username is required')
    elif len(data.get('username', '')) < 3:
        errors.append('Username must be at least 3 characters long')
    
    if not data.get('email'):
        errors.append('Email is required')
    else:
        try:
            validate_email(data['email'])
        except EmailNotValidError:
            errors.append('Invalid email format')
    
    if not data.get('password'):
        errors.append('Password is required')
    elif len(data.get('password', '')) < 6:
        errors.append('Password must be at least 6 characters long')
    
    return errors

def validate_post_data(data):
    """Validate post data"""
    errors = []
    
    if not data.get('title'):
        errors.append('Title is required')
    elif len(data.get('title', '')) < 5:
        errors.append('Title must be at least 5 characters long')
    
    if not data.get('content'):
        errors.append('Content is required')
    elif len(data.get('content', '')) < 10:
        errors.append('Content must be at least 10 characters long')
    
    return errors

def validate_comment_data(data):
    """Validate comment data"""
    errors = []
    
    if not data.get('content'):
        errors.append('Content is required')
    elif len(data.get('content', '')) < 1:
        errors.append('Content cannot be empty')
    
    if not data.get('post_id'):
        errors.append('Post ID is required')
    
    return errors