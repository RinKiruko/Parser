"""add LastUpdateTime

Revision ID: c04156a577e4
Revises: 3bceced658ae
Create Date: 2019-03-28 19:55:10.244381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04156a577e4'
down_revision = '3bceced658ae'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Currencies', sa.Column('LastUpdateTimestamp', sa.Time))


def downgrade():
    pass
