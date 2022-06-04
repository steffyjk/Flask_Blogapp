"""empty message

Revision ID: ce2c0bd2e389
Revises: 4baa792820f1
Create Date: 2022-06-03 14:20:49.361078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce2c0bd2e389'
down_revision = '4baa792820f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.VARCHAR(length=12), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
