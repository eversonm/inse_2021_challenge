"""insert_table_municipio

Revision ID: e6be791bbf4f
Revises: f6ce1e3adee6
Create Date: 2024-01-21 10:38:14.891528

"""
import sqlalchemy as sa
import json
from datetime import datetime
from alembic import op
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean, DateTime, INTEGER


# revision identifiers, used by Alembic.
revision = 'e6be791bbf4f'
down_revision = 'f6ce1e3adee6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = open('src/alembic/versions/municipio.json')
    data = json.load(file)

    municipios = table(
        'municipios',
        column('codigo_m', INTEGER),
        column('federativa_codigo_uf', INTEGER),
        column('nome_m', String),
        column('is_deleted', Boolean),
        column('created_at', DateTime),
        column('updated_at', DateTime),
    )
    op.bulk_insert(
        municipios,
        [
            {
                "codigo_m": obj['codigo_m'],
                "federativa_codigo_uf": obj['federativa_codigo_uf'],
                "nome_m": obj['nome_m'],
                "is_deleted": False,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            for obj in data 
        ]
    )


def downgrade() -> None:
    op.execute('DELETE from municipios')
