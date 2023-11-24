"""add last few columns to posts table

Revision ID: 6ea36b045517
Revises: 763d586e87d5
Create Date: 2023-11-24 16:10:30.290625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ea36b045517'
down_revision: Union[str, None] = '763d586e87d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
