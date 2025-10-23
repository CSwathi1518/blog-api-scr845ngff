from flask import request
from web import db, bcrypt
from web.models.user import User
from web.utils.validators import validate_user_registration
from web.utils.helpers import success_response, error_response
from flask_jwt_extended import create_access_token

def register():
    """Register a new user"""
    try:
        data = request.get_json()
        
        # Validate input
        errors = validate_user_registration(data)
        if errors:
            return error_response('Validation failed', errors, 400)
        
        # Check if user already exists
        if User.query.filter_by(username=data['username']).first():
            return error_response('Username already exists', status=400)
        
        if User.query.filter_by(email=data['email']).first():
            return error_response('Email already exists', status=400)
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        # Create new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return success_response(
            new_user.to_dict(),
            'User registered successfully',
            201
        )
        
    except Exception as e:
        db.session.rollback()
        return error_response(f'Registration failed: {str(e)}', status=500)

def login():
    """Login user and return JWT token"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data.get('username') or not data.get('password'):
            return error_response('Username and password are required', status=400)
        
        # Find user
        user = User.query.filter_by(username=data['username']).first()
        
        if not user or not bcrypt.check_password_hash(user.password, data['password']):
            return error_response('Invalid username or password', status=401)
        
        # Create access token
        access_token = create_access_token(identity=user.id)
        
        return success_response({
            'user': user.to_dict(),
            'access_token': access_token
        }, 'Login successful')
        
    except Exception as e:
        return error_response(f'Login failed: {str(e)}', status=500)