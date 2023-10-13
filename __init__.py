from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.debug = True
    app.secret_key = "kjdanskdjbamsdbakjsndklan"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    from . import sprintr
    app.register_blueprint(sprintr.bp)
    return app

