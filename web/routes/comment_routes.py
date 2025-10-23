from flask import Blueprint
from flask_jwt_extended import jwt_required
from web.controllers import comment_controller

comment_bp = Blueprint('comments', __name__)

# Get comments for a post
comment_bp.route('/comments', methods=['GET'])(comment_controller.get_comments)

# Get single comment
comment_bp.route('/comments/<int:comment_id>', methods=['GET'])(comment_controller.get_comment)

# Create comment (requires authentication)
@comment_bp.route('/comments', methods=['POST'])
@jwt_required()
def create():
    return comment_controller.create_comment()

# Update comment (requires authentication)
@comment_bp.route('/comments/<int:comment_id>', methods=['PUT'])
@jwt_required()
def update(comment_id):
    return comment_controller.update_comment(comment_id)

# Delete comment (requires authentication)
@comment_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete(comment_id):
    return comment_controller.delete_comment(comment_id)