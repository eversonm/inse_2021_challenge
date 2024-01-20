from flask import current_app, Blueprint
from flask_restx import Api

from src.lib.views.start import api as start_namespace


def configure_blueprint():
    blueprint = Blueprint("api", __name__, url_prefix="/")
    authorizations = {
        "apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }

    api = Api(
        blueprint,
        title="INSE API",
        version="1.0.1",
        description="API para consultas do Nível Socieconômico (INSE)",
        authorizations=authorizations,
        security="apikey",
        ordered=True,
    )

    api.add_namespace(start_namespace, path="/start")

    current_app.register_blueprint(blueprint)
