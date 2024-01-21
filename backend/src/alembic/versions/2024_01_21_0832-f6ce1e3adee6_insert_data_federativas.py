"""insert_data_federativas

Revision ID: f6ce1e3adee6
Revises: 70b1042e6a11
Create Date: 2024-01-21 08:32:23.350843

"""
import sqlalchemy as sa
import json
from datetime import datetime
from alembic import op
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean, DateTime, INTEGER


# revision identifiers, used by Alembic.
revision = 'f6ce1e3adee6'
down_revision = '70b1042e6a11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = open('src/alembic/versions/federativo.json')
    data = json.load(file)

    federativa = table(
        'federativas',
        column('codigo_uf', INTEGER),
        column('sigla_uf', String),
        column('nome_uf', String),
        column('is_deleted', Boolean),
        column('created_at', DateTime),
        column('updated_at', DateTime),
    )
    op.bulk_insert(
        federativa,
        [
            {
                "codigo_uf": obj['codigo_uf'],
                "sigla_uf": obj['sigla_uf'],
                "nome_uf": obj['nome_uf'],
                "is_deleted": False,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            for obj in data 
        ]
    )


def downgrade() -> None:
    op.execute('DELETE from federativas')
