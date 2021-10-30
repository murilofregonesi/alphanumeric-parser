import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()

def create_app():

    # App initialization
    app = Flask(__name__)

    APP_MODE = os.environ.get("APP_MODE", "DEV")
    if APP_MODE == 'PRODUCTION':
        app.config.from_object('alpha.instance.config.ProductionConfig')
    elif APP_MODE == 'DEV':
        app.config.from_object('alpha.instance.config.DevelopmentConfig')
    
    app.config['APP_MODE'] = APP_MODE

    with app.app_context():

        # Register blueprints
        from .views import alpha

        app.register_blueprint(alpha)

        return app
