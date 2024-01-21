import humps
from sqlalchemy import Column, String, ForeignKey, INTEGER
from src.lib.models.BaseModel import BaseModel
from src.lib.database.connector_thread import db_session


class Municipios(BaseModel):
    __tablename__ = "municipios"
    codigo_m = Column(INTEGER, primary_key=True, nullable=False, comment="Código do Município")
    federativa_codigo_uf = Column(INTEGER, ForeignKey("federativas.codigo_uf", ondelete="CASCADE"), nullable=False, comment="Sigla da Unidade Federativa")
    nome_m = Column(String, nullable=False, comment="Nome da Unidade Federativa")
    
    @staticmethod
    def get_by_id(_id):
        query = Municipios.query.filter(Municipios.id == _id).first()
        return query.json()

    @staticmethod
    def soft_delete_by_id(_id):
        query = Municipios.query.filter(Municipios.id == _id).first()
        query.is_deleted = True
        db_session.commit()
        
    def to_json(self):
        municipios = self.json()
        del municipios["is_deleted"], municipios["created_at"], municipios["updated_at"]

        return humps.camelize(municipios)
