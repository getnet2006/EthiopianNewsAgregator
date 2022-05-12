from flask import Flask
from News.main import bp as main_bp

# function create app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    return app