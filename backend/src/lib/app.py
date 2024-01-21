from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.lib.views import configure_blueprint
from src.lib.database.connector_thread import db_session


def create_app():
    app = Flask(__name__)
    app.config["SWAGGER_UI_REQUEST_DURATION"] = True
    Bcrypt(app)
    JWTManager(app)

    CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app


if __name__ == "src.lib.app":
    app = create_app()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    with app.app_context():
        configure_blueprint()
        # insert_federativo()

    app.run(host="0.0.0.0", port="5005", debug=True, use_reloader=True)
