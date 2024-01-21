from src.lib.models.Federativas import Federativas
from src.lib.models.Municipios import Municipios
from src.lib.models.Escolas import Escolas
from src.lib.models.PercentualMunicipioEscola import PercentualMunicipioEscola
from src.lib.database.connector_thread import db_session

class FederativasController():
    def get_all(self, *kwargs, **args):

        fed = Federativas.query.all()
        return [row.to_json() for row in fed]