"""media folder links

Revision ID: 37a37072c50d
Revises: 4cbddccc099f
Create Date: 2022-03-21 14:57:34.018532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a37072c50d'
down_revision = '4cbddccc099f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('media_dir', sa.String(length=128), nullable=True))
    op.add_column('jam', sa.Column('file', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jam', 'file')
    op.drop_column('event', 'media_dir')
    # ### end Alembic commands ###