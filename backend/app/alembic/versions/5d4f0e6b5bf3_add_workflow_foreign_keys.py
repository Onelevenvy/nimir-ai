"""add workflow foreign keys

Revision ID: 5d4f0e6b5bf3
Revises: bed7d0a5efc0
Create Date: 2024-11-05 09:20:50.623964

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '5d4f0e6b5bf3'
down_revision = 'bed7d0a5efc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'data', 'workflow_execution', ['workflow_execution_id'], ['execution_id'])
    op.create_foreign_key(None, 'data', 'workflow_node_execution', ['node_execution_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'data', type_='foreignkey')
    op.drop_constraint(None, 'data', type_='foreignkey')
    # ### end Alembic commands ###
