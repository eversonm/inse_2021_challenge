import humps
from src.lib.models.Escolas import Escolas
from src.lib.models.Federativas import Federativas
from src.lib.models.Municipios import Municipios
from src.lib.models.PercentualMunicipioEscola import PercentualMunicipioEscola
from src.lib.database.connector_thread import db_session

class EscolasController():
    def get(self, codigo_e):
        escolas = db_session.query(
            Escolas, 
            Federativas, 
            Municipios,
            PercentualMunicipioEscola
        ).join(
            Municipios, 
            Escolas.municipio_codigo_m==Municipios.codigo_m
        ).join(
            Federativas,
            Municipios.federativa_codigo_uf==Federativas.codigo_uf
        ).join(
            PercentualMunicipioEscola,
            Escolas.codigo_e==PercentualMunicipioEscola.escola_codigo_e
        ).with_entities(
            Escolas.codigo_e,
            Escolas.nome_e,
            Escolas.tipo_rede,
            Escolas.tipo_localizacao,
            Escolas.tipo_capital,
            Escolas.inse_classificacao,
            Escolas.qtde_alunos,
            Escolas.media_inse,
            Municipios.codigo_m,
            Municipios.nome_m,
            Federativas.codigo_uf,
            Federativas.sigla_uf,
            Federativas.nome_uf,
            PercentualMunicipioEscola.percentual_nivel_1,
            PercentualMunicipioEscola.percentual_nivel_2,
            PercentualMunicipioEscola.percentual_nivel_3,
            PercentualMunicipioEscola.percentual_nivel_4,
            PercentualMunicipioEscola.percentual_nivel_5,
            PercentualMunicipioEscola.percentual_nivel_6,
            PercentualMunicipioEscola.percentual_nivel_7,
            PercentualMunicipioEscola.percentual_nivel_8,
        ).filter(
            Escolas.codigo_e == codigo_e
        ).first()

        escola = humps.camelize({
            "codigo_e": escolas[0],
            "nome_e": escolas[1],
            "tipo_rede": escolas[2].name,
            "tipo_localizacao": escolas[3].name,
            "tipo_capital": escolas[4].name,
            "inse_classificacao": escolas[5].name,
            "qtde_alunos": escolas[6],
            "media_inse": escolas[7],
            "codigo_m": escolas[8],
            "nome_m": escolas[9],
            "codigo_uf": escolas[10],
            "sigla_uf": escolas[11],
            "nome_uf": escolas[12],
            "percentual_nivel_1": escolas[13],
            "percentual_nivel_2": escolas[14],
            "percentual_nivel_3": escolas[15],
            "percentual_nivel_4": escolas[16],
            "percentual_nivel_5": escolas[17],
            "percentual_nivel_6": escolas[18],
            "percentual_nivel_7": escolas[19],
            "percentual_nivel_8": escolas[20],
            })
        
        return escola