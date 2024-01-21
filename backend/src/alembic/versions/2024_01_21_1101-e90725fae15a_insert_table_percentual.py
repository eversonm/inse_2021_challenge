"""insert_table_percentual

Revision ID: e90725fae15a
Revises: 21a88419e0dd
Create Date: 2024-01-21 11:01:46.220656

"""
import json
from datetime import datetime
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import  Boolean, DateTime, INTEGER, Float


# revision identifiers, used by Alembic.
revision = 'e90725fae15a'
down_revision = '21a88419e0dd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = open('src/alembic/versions/percentual.json')
    data = json.load(file)

    percentual = table(
        'percentual_municipios_escolas',
        column('escola_codigo_e', INTEGER),
        column('municipio_codigo_m', INTEGER),
        column('percentual_nivel_1', Float),
        column('percentual_nivel_2', Float),
        column('percentual_nivel_3', Float),
        column('percentual_nivel_4', Float),
        column('percentual_nivel_5', Float),
        column('percentual_nivel_6', Float),
        column('percentual_nivel_7', Float),
        column('percentual_nivel_8', Float),
        column('is_deleted', Boolean),
        column('created_at', DateTime),
        column('updated_at', DateTime),
    )
    op.bulk_insert(
        percentual,
        [
            {
                "escola_codigo_e": obj['escola_codigo_e'],
                "municipio_codigo_m": obj['municipio_codigo_m'],
                "percentual_nivel_1": obj['percentual_nivel_1'],
                "percentual_nivel_2": obj['percentual_nivel_2'],
                "percentual_nivel_3": obj['percentual_nivel_3'],
                "percentual_nivel_4": obj['percentual_nivel_4'],
                "percentual_nivel_5": obj['percentual_nivel_5'],
                "percentual_nivel_6": obj['percentual_nivel_6'],
                "percentual_nivel_7": obj['percentual_nivel_7'],
                "percentual_nivel_8": obj['percentual_nivel_8'],
                "is_deleted": False,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            for obj in data 
        ]
    )


def downgrade() -> None:
    op.execute('DELETE from percentual_municipios_escolas')
