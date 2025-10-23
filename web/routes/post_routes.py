from flask import Blueprint
from flask_jwt_extended import jwt_required
from web.controllers import post_controller

post_bp = Blueprint('posts', __name__)

# Get all posts
post_bp.route('/posts', methods=['GET'])(post_controller.get_all_posts)

# Get single post
post_bp.route('/posts/<int:post_id>', methods=['GET'])(post_controller.get_post)

# Create post (requires authentication)
@post_bp.route('/posts', methods=['POST'])
@jwt_required()
def create():
    return post_controller.create_post()

# Update post (requires authentication)
@post_bp.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update(post_id):
    return post_controller.update_post(post_id)

# Delete post (requires authentication)
@post_bp.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete(post_id):
    return post_controller.delete_post(post_id)