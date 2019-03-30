"""create currency table

Revision ID: 04d0d0125519
Revises: 
Create Date: 2019-03-27 22:22:33.012889

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import Integer, String, Date
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision = '04d0d0125519'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Currencies',
        sa.Column('ID', Integer, primary_key=True),
        sa.Column('Title', String, unique=True),
        sa.Column('Symbol', String, unique=True),
        sa.Column('ListingDate', Date),
        sa.Column('Market', JSON),
        sa.Column('Url', String)
    )


def downgrade():
    op.drop_table('Currencies')
