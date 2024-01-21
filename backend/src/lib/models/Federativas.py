import humps
from sqlalchemy import Column, String, INTEGER
from src.lib.models.BaseModel import BaseModel
from src.lib.database.connector_thread import db_session


class Federativas(BaseModel):
    __tablename__ = "federativas"
    codigo_uf = Column(INTEGER, primary_key=True, nullable=False, comment="Código da Unidade Federativa")
    sigla_uf = Column(String, nullable=False, comment="Sigla da Unidade Federativa")
    nome_uf = Column(String, nullable=False, comment="Nome da Unidade Federativa")
    
    @staticmethod
    def get_by_id(_id):
        query = Federativas.query.filter(Federativas.id == _id).first()
        return query.json()

    @staticmethod
    def soft_delete_by_id(_id):
        query = Federativas.query.filter(Federativas.id == _id).first()
        query.is_deleted = True
        db_session.commit()
        
    def to_json(self):
        federativas = self.json()
        del federativas["is_deleted"], federativas["created_at"], federativas["updated_at"]

        return humps.camelize(federativas)
