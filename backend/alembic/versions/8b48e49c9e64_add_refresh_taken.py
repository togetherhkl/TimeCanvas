"""add refresh_taken

Revision ID: 8b48e49c9e64
Revises: a175e6b85fe9
Create Date: 2024-01-29 12:18:41.019327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b48e49c9e64'
down_revision: Union[str, None] = 'a175e6b85fe9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
