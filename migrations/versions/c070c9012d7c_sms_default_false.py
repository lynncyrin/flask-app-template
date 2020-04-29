"""sms default false

Revision ID: c070c9012d7c
Revises: 3f49b98b1a24
Create Date: 2020-04-29 06:54:56.798923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c070c9012d7c'
down_revision = '3f49b98b1a24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'smsUser',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'smsUser',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
