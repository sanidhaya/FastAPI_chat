"""add content column to posts table

Revision ID: 075442b4bd44
Revises: 52a3d2d31f06
Create Date: 2023-11-23 19:22:23.065387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '075442b4bd44'
down_revision: Union[str, None] = '52a3d2d31f06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
