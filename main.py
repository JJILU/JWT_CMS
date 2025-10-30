from flask import Flask
from extensions import db,migrate,jwt
from dotenv import load_dotenv

load_dotenv()


def create_app():
    
    app = Flask(__name__)

    # app config
    app.config.from_prefixed_env()

    # init extensions
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)


    # import blueprint and register
    from app.auth.views import auth_bp
    from app.dash.views import dash_bp


    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(dash_bp, url_prefix="/dash")

    return app