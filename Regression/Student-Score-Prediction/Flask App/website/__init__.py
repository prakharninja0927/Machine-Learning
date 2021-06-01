from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']="asdfgh hgfdsa"

    from .score import score
    app.register_blueprint(score,url_prefix="/")

    return app
