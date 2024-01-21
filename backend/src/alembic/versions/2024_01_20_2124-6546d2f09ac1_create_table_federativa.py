"""create_table_federativa

Revision ID: 6546d2f09ac1
Revises: 
Create Date: 2024-01-20 21:24:32.389808

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '6546d2f09ac1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "federativas",
        sa.Column("codigo_uf", 
                  postgresql.INTEGER(), 
                  autoincrement=False, 
                  nullable=False,
                  comment="Código da Unidade Federativa"),
        sa.Column(
            "sigla_uf",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment="Sigla da Unidade Federativa"
        ),
        sa.Column(
            "nome_uf",
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
        sa.PrimaryKeyConstraint("codigo_uf", name="federativa_pkey"),
    )


def downgrade() -> None:
    op.drop_table("federativas")
