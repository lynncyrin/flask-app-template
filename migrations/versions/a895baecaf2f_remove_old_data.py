"""remove old data

Revision ID: a895baecaf2f
Revises: 79d8f23d7fe1
Create Date: 2020-04-29 01:13:00.333491

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'a895baecaf2f'
down_revision = '79d8f23d7fe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
