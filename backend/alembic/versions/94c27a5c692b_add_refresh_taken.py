"""add refresh_taken

Revision ID: 94c27a5c692b
Revises: 6078e0ac1012
Create Date: 2024-01-29 12:09:51.853885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94c27a5c692b'
down_revision: Union[str, None] = '6078e0ac1012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("refresh_token", sa.String(500), nullable=False))


def downgrade() -> None:
    pass
