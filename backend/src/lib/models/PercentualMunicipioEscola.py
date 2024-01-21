import humps
from sqlalchemy import Column, FLOAT, ForeignKey, INTEGER, PrimaryKeyConstraint
from src.lib.models.BaseModel import BaseModel
from src.lib.database.connector_thread import db_session


class PercentualMunicipioEscola(BaseModel):
    __tablename__ = "percentual_municipios_escolas"
    __table_args__ = (
        PrimaryKeyConstraint('escola_codigo_e', 'municipio_codigo_m'),
    )
    escola_codigo_e = Column(INTEGER, 
                                  ForeignKey("escolas.codigo_e", ondelete="CASCADE"), 
                                  nullable=False, 
                                  comment="Código da escola"
                                  )
    municipio_codigo_m = Column(INTEGER, 
                                ForeignKey("municipios.codigo_m", ondelete="CASCADE"), 
                                nullable=False, 
                                comment="Código do municipio")
    percentual_nivel_1 = Column(FLOAT, nullable=False)
    percentual_nivel_2 = Column(FLOAT, nullable=False)
    percentual_nivel_3 = Column(FLOAT, nullable=False)
    percentual_nivel_4 = Column(FLOAT, nullable=False)
    percentual_nivel_5 = Column(FLOAT, nullable=False)
    percentual_nivel_6 = Column(FLOAT, nullable=False)
    percentual_nivel_7 = Column(FLOAT, nullable=False)
    percentual_nivel_8 = Column(FLOAT, nullable=False)
        
    def to_json(self):
        percentual = self.json()
        del percentual["is_deleted"], percentual["created_at"], percentual["updated_at"]

        return humps.camelize(percentual)
