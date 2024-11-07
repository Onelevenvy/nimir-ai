"""update workflow tabel4

Revision ID: aba76c53c7fa
Revises: 3a283e23a07e
Create Date: 2024-11-02 18:02:03.417274

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "aba76c53c7fa"
down_revision = "3a283e23a07e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("data_processing_chain")
    op.drop_constraint(
        "processed_data_input_data_id_fkey", "processed_data", type_="foreignkey"
    )
    op.drop_column("processed_data", "input_data_id")
    op.alter_column(
        "workflow_execution",
        "workflow_version",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "workflow_execution",
        "config",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
    )
    op.alter_column(
        "workflow_execution",
        "started_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    op.alter_column(
        "workflow_node_execution",
        "config",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "workflow_node_execution",
        "config",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
    )
    op.alter_column(
        "workflow_execution",
        "started_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    op.alter_column(
        "workflow_execution",
        "config",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
    )
    op.alter_column(
        "workflow_execution",
        "workflow_version",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.add_column(
        "processed_data",
        sa.Column("input_data_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "processed_data_input_data_id_fkey",
        "processed_data",
        "processed_data",
        ["input_data_id"],
        ["id"],
    )
    op.create_table(
        "data_processing_chain",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "original_data_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "processed_data_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.Column("execution_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "processing_order", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["execution_id"],
            ["workflow_execution.execution_id"],
            name="data_processing_chain_execution_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["original_data_id"],
            ["data.data_id"],
            name="data_processing_chain_original_data_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["processed_data_id"],
            ["processed_data.id"],
            name="data_processing_chain_processed_data_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="data_processing_chain_pkey"),
    )
    # ### end Alembic commands ###
