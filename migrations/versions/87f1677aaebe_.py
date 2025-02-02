"""empty message

Revision ID: 87f1677aaebe
Revises: f19d8f567868
Create Date: 2025-01-30 19:18:54.088474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f1677aaebe'
down_revision = 'f19d8f567868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('origin_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('location_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'locations', ['origin_id'], ['id'])
        batch_op.create_foreign_key(None, 'locations', ['location_id'], ['id'])
        batch_op.drop_column('location')
        batch_op.drop_column('origin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('origin', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('location_id')
        batch_op.drop_column('origin_id')

    # ### end Alembic commands ###
