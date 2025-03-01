"""update workflow tabel

Revision ID: 8da2477d07b6
Revises: bcb1c618907d
Create Date: 2024-11-02 09:21:37.784281

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8da2477d07b6"
down_revision = "bcb1c618907d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "workflow_node_execution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("execution_id", sa.Integer(), nullable=False),
        sa.Column("node_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("node_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "PROCESSING",
                "COMPLETED",
                "FAILED",
                "SKIPPED",
                name="nodestatus",
            ),
            nullable=False,
        ),
        sa.Column("config", sa.JSON(), nullable=False),
        sa.Column("input_data_ids", sa.JSON(), nullable=False),
        sa.Column("output_data_ids", sa.JSON(), nullable=False),
        sa.Column("error_message", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["execution_id"],
            ["workflow_execution.execution_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "processed_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("original_data_id", sa.Integer(), nullable=False),
        sa.Column("node_execution_id", sa.Integer(), nullable=False),
        sa.Column("file_path", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("file_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("format", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("metadata_", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["node_execution_id"],
            ["workflow_node_execution.id"],
        ),
        sa.ForeignKeyConstraint(
            ["original_data_id"],
            ["data.data_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "data_processing_chain",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("original_data_id", sa.Integer(), nullable=False),
        sa.Column("processed_data_id", sa.Integer(), nullable=False),
        sa.Column("execution_id", sa.Integer(), nullable=False),
        sa.Column("processing_order", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["execution_id"],
            ["workflow_execution.execution_id"],
        ),
        sa.ForeignKeyConstraint(
            ["original_data_id"],
            ["data.data_id"],
        ),
        sa.ForeignKeyConstraint(
            ["processed_data_id"],
            ["processed_data.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("project", sa.Column("current_workflow", sa.JSON(), nullable=True))
    op.add_column("project", sa.Column("workflow_version", sa.Integer(), nullable=True))
    op.alter_column(
        "workflow", "project_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.add_column(
        "workflow_execution", sa.Column("project_id", sa.Integer(), nullable=True)
    )
    op.add_column(
        "workflow_execution",
        sa.Column("workflow_version", sa.Integer(), nullable=True),
    )
    op.add_column("workflow_execution", sa.Column("config", sa.JSON(), nullable=True))
    op.add_column(
        "workflow_execution", sa.Column("started_at", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "workflow_execution", sa.Column("completed_at", sa.DateTime(), nullable=True)
    )
    op.alter_column(
        "workflow_execution",
        "status",
        existing_type=postgresql.ENUM(
            "PENDING", "RUNNING", "COMPLETED", "FAILED", name="workflowstatus"
        ),
        type_=sqlmodel.sql.sqltypes.AutoString(),
        existing_nullable=False,
    )
    op.create_foreign_key(
        None, "workflow_execution", "project", ["project_id"], ["project_id"]
    )
    op.drop_column("workflow_execution", "result")
    op.drop_column("workflow_execution", "start_time")
    op.drop_column("workflow_execution", "end_time")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "workflow_execution",
        sa.Column(
            "end_time", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "workflow_execution",
        sa.Column(
            "start_time", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "workflow_execution",
        sa.Column(
            "result",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_constraint(None, "workflow_execution", type_="foreignkey")
    op.alter_column(
        "workflow_execution",
        "status",
        existing_type=sqlmodel.sql.sqltypes.AutoString(),
        type_=postgresql.ENUM(
            "PENDING", "RUNNING", "COMPLETED", "FAILED", name="workflowstatus"
        ),
        existing_nullable=False,
    )
    op.drop_column("workflow_execution", "completed_at")
    op.drop_column("workflow_execution", "started_at")
    op.drop_column("workflow_execution", "config")
    op.drop_column("workflow_execution", "workflow_version")
    op.drop_column("workflow_execution", "project_id")
    op.alter_column("workflow", "project_id", existing_type=sa.INTEGER(), nullable=True)
    op.drop_column("project", "workflow_version")
    op.drop_column("project", "current_workflow")
    op.drop_table("data_processing_chain")
    op.drop_table("processed_data")
    op.drop_table("workflow_node_execution")
    # ### end Alembic commands ###
