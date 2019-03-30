"""add Deals column

Revision ID: 3bceced658ae
Revises: 04d0d0125519
Create Date: 2019-03-28 18:05:34.733423

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import HSTORE

# revision identifiers, used by Alembic.
revision = '3bceced658ae'
down_revision = '04d0d0125519'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Currencies', sa.Column('Deals',HSTORE))


def downgrade():
    pass
