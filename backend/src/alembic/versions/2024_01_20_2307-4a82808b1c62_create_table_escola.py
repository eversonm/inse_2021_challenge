"""create_table_escola

Revision ID: 4a82808b1c62
Revises: 063bf2bcc8a3
Create Date: 2024-01-20 23:07:58.873872

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '4a82808b1c62'
down_revision = '063bf2bcc8a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "escolas",
        sa.Column(
            "codigo_e", 
            postgresql.INTEGER(), 
            autoincrement=False, 
            nullable=False,
            comment="Código da Escola"
            ),
        sa.Column(
            "nome_e",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment="Nome da Escola",
            ),
        sa.Column(
            'tipo_rede', 
            sa.Enum('Estadual', 'Federal', 'Municipal', name='escola_tipo_rede'), 
            nullable=False
            ),
        sa.Column(
            'tipo_localizacao', 
            sa.Enum('Urbana', 'Rural', name='escola_tipo_localizacao'), 
            nullable=False
            ),
        sa.Column(
            'tipo_capital', 
            sa.Enum('Capital', 'Interior', name='escola_tipo_capital'), 
            nullable=False
            ),
        sa.Column(
            "qtde_alunos", 
            postgresql.INTEGER(), 
            autoincrement=False, 
            nullable=False,
            comment="Quantidade de Alunos com INSE calculado utilizado para o cálculo das médias por escola"
            ),
        sa.Column(
            "media_inse", 
            postgresql.FLOAT(), 
            nullable=False,
            comment="Média do Indicador de Nível Socioeconômico dos alunos da escola"
            ),
        sa.Column(
            "inse_classificacao",
            sa.Enum(
                'Nível I', 
                'Nível II', 
                'Nível III',
                'Nível IV',
                'Nível V',
                'Nível VI',
                'Nível VII',
                'Nível VIII',
                name='escola_inse_classificacao'
                ), 
            autoincrement=False,
            nullable=False,
            comment="Classificação do Indicador de Nível Socioeconômico (8 grupos)",
            ),
        sa.Column(
            "municipio_codigo_m",
            postgresql.INTEGER(), 
            autoincrement=False,
            nullable=False,
            comment="Código do Municipio"
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
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
            ),
        sa.PrimaryKeyConstraint("codigo_e", name="escola_pkey"),
        sa.ForeignKeyConstraint(
            ["municipio_codigo_m"],
            ["municipios.codigo_m"],
            name="municipio_codigo_m_fkey",
            ondelete="CASCADE",
            ),
    )


def downgrade() -> None:
    op.drop_table("escolas")
