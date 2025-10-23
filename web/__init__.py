from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    
    # Register blueprints
    with app.app_context():
        from web.routes.auth_routes import auth_bp
        from web.routes.post_routes import post_bp
        from web.routes.comment_routes import comment_bp
        
        app.register_blueprint(auth_bp, url_prefix='/api/auth')
        app.register_blueprint(post_bp, url_prefix='/api')
        app.register_blueprint(comment_bp, url_prefix='/api')
    
    # Home route
    @app.route('/')
    def home():
        return {
            'message': 'Blog API is running',
            'version': '1.0.0',
            'endpoints': {
                'auth': '/api/auth',
                'posts': '/api/posts',
                'comments': '/api/comments'
            }
        }, 200
    
    return app