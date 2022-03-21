"""restart + expanded event model

Revision ID: 4cbddccc099f
Revises: 
Create Date: 2022-03-18 19:45:47.419487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cbddccc099f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('street_address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=8), nullable=True),
    sa.Column('zip', sa.SmallInteger(), nullable=True),
    sa.Column('info', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('event_door', sa.DateTime(), nullable=True),
    sa.Column('event_start', sa.DateTime(), nullable=True),
    sa.Column('event_end', sa.DateTime(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(precision=2), nullable=False),
    sa.Column('ticket_link', sa.String(length=512), nullable=True),
    sa.Column('ages', sa.String(length=8), nullable=True),
    sa.Column('about', sa.String(length=2048), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_updated'), 'event', ['updated'], unique=False)
    op.create_table('jam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('track_num', sa.SmallInteger(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jam')
    op.drop_index(op.f('ix_event_updated'), table_name='event')
    op.drop_table('event')
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###