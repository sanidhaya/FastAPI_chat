"""add user table

Revision ID: 7360058113b7
Revises: 075442b4bd44
Create Date: 2023-11-23 19:27:37.641371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7360058113b7'
down_revision: Union[str, None] = '075442b4bd44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(), nullable = False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email')
                            )
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
