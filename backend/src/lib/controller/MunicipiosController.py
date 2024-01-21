from src.lib.models.Municipios import Municipios

class MunicipiosController():
    def get(self, codigo_uf):
        municipios = Municipios.query.filter(
            Municipios.federativa_codigo_uf==codigo_uf
            ).all()
        return [row.to_json() for row in municipios]