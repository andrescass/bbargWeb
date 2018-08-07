"""empty message

Revision ID: bd5e75901a40
Revises: bda2137609f8
Create Date: 2018-08-06 15:38:02.986482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5e75901a40'
down_revision = 'bda2137609f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('is_chart', sa.Boolean(), nullable=True))
    op.add_column('employees', sa.Column('is_lore', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'is_lore')
    op.drop_column('employees', 'is_chart')
    # ### end Alembic commands ###