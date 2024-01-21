"""insert_table_escolas

Revision ID: 21a88419e0dd
Revises: e6be791bbf4f
Create Date: 2024-01-21 10:45:12.644842

"""
import sqlalchemy as sa
import json
from datetime import datetime
from alembic import op
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean, DateTime, INTEGER, Enum, Float


# revision identifiers, used by Alembic.
revision = '21a88419e0dd'
down_revision = 'e6be791bbf4f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = open('src/alembic/versions/escolas.json')
    data = json.load(file)

    escolas = table(
        'escolas',
        column('codigo_e', INTEGER),
        column('nome_e', String),
        column('tipo_rede', Enum),
        column('tipo_localizacao', Enum),
        column('tipo_capital', Enum),
        column('inse_classificacao', Enum),
        column('qtde_alunos', INTEGER),
        column('media_inse', Float),
        column('municipio_codigo_m', INTEGER),
        column('is_deleted', Boolean),
        column('created_at', DateTime),
        column('updated_at', DateTime),
    )
    op.bulk_insert(
        escolas,
        [
            {
                "codigo_e": obj['codigo_e'],
                "nome_e": obj['nome_e'],
                "tipo_rede": obj['tipo_rede'],
                "tipo_localizacao": obj['tipo_localizacao'],
                "tipo_capital": obj['tipo_capital'],
                "inse_classificacao": obj['inse_classificacao'],
                "qtde_alunos": obj['qtde_alunos'],
                "media_inse": obj['media_inse'],
                "municipio_codigo_m": obj['municipio_codigo_m'],
                "is_deleted": False,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            for obj in data 
        ]
    )


def downgrade() -> None:
    op.execute('DELETE from escolas')
