"""create_table_percentual_municipio_escola

Revision ID: 70b1042e6a11
Revises: 4a82808b1c62
Create Date: 2024-01-20 23:20:13.460908

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '70b1042e6a11'
down_revision = '4a82808b1c62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "percentual_municipios_escolas",
        sa.Column(
            "municipio_codigo_m", 
            postgresql.INTEGER(), 
            autoincrement=False, 
            nullable=False,
            comment="Código do Município"
            ),
        sa.Column(
            "escola_codigo_e", 
            postgresql.INTEGER(), 
            autoincrement=False, 
            nullable=False,
            comment="Código da Escola"
            ),
        sa.Column(
            "percentual_nivel_1", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível I."
            ),
        sa.Column(
            "percentual_nivel_2", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível II."
            ),
        sa.Column(
            "percentual_nivel_3", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível III."
            ),
        sa.Column(
            "percentual_nivel_4", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível IV."
            ),
        sa.Column(
            "percentual_nivel_5", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível V."
            ),
        sa.Column(
            "percentual_nivel_6", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível VI."
            ),
        sa.Column(
            "percentual_nivel_7", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível VII."
            ),
        sa.Column(
            "percentual_nivel_8", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Percentual de alunos da Escola classificados no Nível VIII."
            ),
        sa.Column(
            "is_deleted",
            sa.BOOLEAN(),
            autoincrement=False,
            nullable=False,
            ),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
            ),
        sa.Column(''
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
            ),
        sa.ForeignKeyConstraint(
            ["municipio_codigo_m"],
            ["municipios.codigo_m"],
            name="municipio_codigo_m_fkey",
            ondelete="CASCADE",
            ),
        sa.ForeignKeyConstraint(
            ["escola_codigo_e"],
            ["escolas.codigo_e"],
            name="escola_codigo_e_fkey",
            ondelete="CASCADE",
            ),
    )
    op.create_primary_key(
        'percentual_municipios_escolas_pkey', 
        'percentual_municipios_escolas', 
        ['municipio_codigo_m', 'escola_codigo_e'])


def downgrade() -> None:
    op.drop_table("percentual_municipios_escolas")