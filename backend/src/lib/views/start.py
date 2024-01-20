from flask_restx import Resource
from src.lib.schemas.StartDto import StartDto

api = StartDto.api


@api.route("")
class InseTest(Resource):
    @api.doc("Only for swagger test")
    def get(self):
        return {"message": "System on!"}, 200
