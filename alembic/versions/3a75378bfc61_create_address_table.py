"""create address table

Revision ID: 3a75378bfc61
Revises: bb24e6923efa
Create Date: 2023-04-24 11:37:47.907425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a75378bfc61'
down_revision = 'bb24e6923efa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('City', sa.String(), nullable=False),
                    sa.Column('Area', sa.String(), nullable=False),
                    sa.Column('Country', sa.String(), nullable=False),
                    sa.Column('Postcode', sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
