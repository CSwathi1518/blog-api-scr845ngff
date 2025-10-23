from flask import Blueprint
from web.controllers import auth_controller

auth_bp = Blueprint('auth', __name__)

# Register route
auth_bp.route('/register', methods=['POST'])(auth_controller.register)

# Login route
auth_bp.route('/login', methods=['POST'])(auth_controller.login)