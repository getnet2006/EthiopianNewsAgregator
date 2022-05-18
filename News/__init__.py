from flask import Flask
from News.main import bp as main_bp
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

# function create app
def create_app():
    app = Flask(__name__)
    # initialize bootstrap
    bootstrap.init_app(app)
    # register blueprint
    app.register_blueprint(main_bp)
    
    return app