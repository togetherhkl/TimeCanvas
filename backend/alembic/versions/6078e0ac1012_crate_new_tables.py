"""crate new tables

Revision ID: 6078e0ac1012
Revises: 3dc479c359e5
Create Date: 2024-01-28 15:41:33.029870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6078e0ac1012'
down_revision: Union[str, None] = '3dc479c359e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
