import enum
import humps
from sqlalchemy import Column, ForeignKey, String, INTEGER, FLOAT, Enum
from src.lib.models.BaseModel import BaseModel
from src.lib.database.connector_thread import db_session

class TipoRede(enum.Enum):
    Federal = 1
    Estadual = 2
    Municipal = 3


class TipoLocalizacao(enum.Enum):
    Urbana = 1
    Rural = 2


class TipoCapital(enum.Enum):
    Capital = 1
    Interior = 2


InseClassificacao = enum.Enum(
    value='InseClassificacao',
    names=[
        ("Nível I", 1),
        ("Nível II", 2),
        ("Nível III", 3),
        ("Nível IV", 4),
        ("Nível V", 5),
        ("Nível VI", 6),
        ("Nível VII", 7),
        ("Nível VIII", 8),
    ]
)


class Escolas(BaseModel):
    __tablename__ = "escolas"
    codigo_e = Column(INTEGER, primary_key=True, nullable=False, comment="Código da escola")
    nome_e = Column(String, nullable=False, comment="Nome da Escola")
    tipo_rede = Column(Enum(TipoRede))
    tipo_localizacao = Column(Enum(TipoLocalizacao))
    tipo_capital = Column(Enum(TipoCapital))
    inse_classificacao = Column(Enum(InseClassificacao))
    qtde_alunos = Column(INTEGER, nullable=False, comment="Quantidade de Alunos com INSE calculado")
    media_inse = Column(FLOAT, nullable=False, comment="Média do Indicador de Nível Socioeconômico dos alunos da escola")
    municipio_codigo_m = Column(INTEGER, ForeignKey("municipios.codigo_m", ondelete="CASCADE"), nullable=False, comment="Código do municipio")

    @staticmethod
    def get_by_id(_id):
        query = Escolas.query.filter(Escolas.id == _id).first()
        return query.json()

    @staticmethod
    def soft_delete_by_id(_id):
        query = Escolas.query.filter(Escolas.id == _id).first()
        query.is_deleted = True
        db_session.commit()
        
    def to_json(self):
        escolas = self.json()
        escolas['tipo_rede'] = str(self.tipo_rede.name)
        escolas['tipo_localizacao'] = str(self.tipo_localizacao.name)
        escolas['tipo_capital'] = str(self.tipo_capital.name)
        escolas['inse_classificacao'] = str(self.inse_classificacao.name)
        del escolas["is_deleted"], escolas["created_at"], escolas["updated_at"]

        return humps.camelize(escolas)
