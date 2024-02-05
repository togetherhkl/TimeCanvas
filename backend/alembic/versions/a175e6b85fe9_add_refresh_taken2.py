"""add refresh_taken2

Revision ID: a175e6b85fe9
Revises: 94c27a5c692b
Create Date: 2024-01-29 12:13:11.387994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a175e6b85fe9'
down_revision: Union[str, None] = '94c27a5c692b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("refresh_token", sa.String(500), nullable=False))


def downgrade() -> None:
    pass
