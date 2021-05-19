"""create-users

Revision ID: 3e1cf7855395
Revises: 
Create Date: 2021-05-19 08:18:22.831534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1cf7855395'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String),
    )


def downgrade():
    op.drop_table('users')
