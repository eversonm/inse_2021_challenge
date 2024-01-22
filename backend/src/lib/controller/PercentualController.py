import humps
from src.lib.models.Escolas import Escolas
from src.lib.models.Federativas import Federativas
from src.lib.models.Municipios import Municipios
from src.lib.models.PercentualMunicipioEscola import PercentualMunicipioEscola
from src.lib.database.connector_thread import db_session

class PercentualController():
    def get_top_10_worst(self):
        percentual = db_session.query(
            PercentualMunicipioEscola,
            Federativas, 
            Municipios,
        ).join(
            Municipios, 
            Escolas.municipio_codigo_m==Municipios.codigo_m
        ).join(
            Federativas,
            Municipios.federativa_codigo_uf==Federativas.codigo_uf
        )
        return percentual