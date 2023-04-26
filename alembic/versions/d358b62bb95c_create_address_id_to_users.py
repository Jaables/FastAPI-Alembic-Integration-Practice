"""create address id to users

Revision ID: d358b62bb95c
Revises: 3a75378bfc61
Create Date: 2023-04-24 11:50:43.830736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd358b62bb95c'
down_revision = '3a75378bfc61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_user_fk', source_table="users", referent_table="address", local_cols=["address_id"],
                          remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')