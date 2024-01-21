from flask import request
from flask_restx import Resource
from src.lib.schemas.StartDto import StartDto
from src.lib.controller.QueryController import QueryController
from src.lib.controller.FederativasController import FederativasController
from src.lib.controller.MunicipiosController import MunicipiosController
from src.lib.controller.EscolasController import EscolasController
api = StartDto.api


@api.route("/filter")
class InseTest(Resource):
    @api.doc("Listar tudo")
    def get(self):
        dict_busca = {}
        dict_busca["page"] = int(request.args.get("page"))
        dict_busca["federacao"] = int(request.args.get("federacao", 0))
        dict_busca["municipio"] = int(request.args.get("municipio", 0))
        dict_busca["rede"] = int(request.args.get("rede", 0))
        dict_busca["localizacao"] = int(request.args.get("localizacao", 0))
        dict_busca["capital"] = int(request.args.get("capital", 0))
        dict_busca["classificacao"] = int(request.args.get("classificacao", 0))
        dict_busca["search"] = request.args.get("search", "")

        query = QueryController()
        query_ = query.get_all_json(**dict_busca)
        return query_, 200


@api.route("/federativas")
class InseFederacoes(Resource):
    @api.doc("Listar os estados")
    def get(self):
        query = FederativasController()
        query_ = query.get_all()
        return query_, 200


@api.route("/municipios/<codigo_uf>")
class InsetMunicipios(Resource):
    @api.doc("Listar municipios de um estado")
    def get(self, codigo_uf):
        query = MunicipiosController()
        query_ = query.get(codigo_uf)
        return query_, 200


@api.route("/escola/<codigo_e>")
class InsetEscola(Resource):
    @api.doc("Listar uma escola")
    def get(self, codigo_e):
        query = EscolasController()
        query_ = query.get(codigo_e)
        return query_, 200
