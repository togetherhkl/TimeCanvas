"""create relationship

Revision ID: 2b1450d6e543
Revises: da139570e913
Create Date: 2024-02-08 11:21:54.347217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b1450d6e543'
down_revision: Union[str, None] = 'da139570e913'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
