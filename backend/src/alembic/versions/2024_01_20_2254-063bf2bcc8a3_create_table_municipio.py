"""create_table_municipio

Revision ID: 063bf2bcc8a3
Revises: 6546d2f09ac1
Create Date: 2024-01-20 22:54:25.410671

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '063bf2bcc8a3'
down_revision = '6546d2f09ac1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "municipios",
        sa.Column(
            "codigo_m", 
            postgresql.INTEGER(), 
            autoincrement=False, 
            nullable=False,
            comment="Código do Município"),
        sa.Column(
            "federativa_codigo_uf",
            postgresql.INTEGER(), 
            autoincrement=False,
            nullable=False,
            comment="Código da Unidade Federativa"
        ),
        sa.Column(
            "nome_m",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment="Nome da Unidade Federativa",
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
        sa.PrimaryKeyConstraint("codigo_m", name="municipio_pkey"),
        sa.ForeignKeyConstraint(
            ["federativa_codigo_uf"],
            ["federativas.codigo_uf"],
            name="federativa_codigo_uf_fkey",
            ondelete="CASCADE",
        ),
    )


def downgrade() -> None:
    op.drop_table("municipios")
