from flask import Flask
from flask_refactor.routes.main import main_bp
from flask_refactor.routes.api import api_bp

def create_app():
    app = Flask(__name__, 
                template_folder='flask_refactor/templates',
                static_folder='flask_refactor/static')
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
