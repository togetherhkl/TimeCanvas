"""add-deftime

Revision ID: 0bc878fa2851
Revises: ba3859b8f107
Create Date: 2024-03-08 14:49:09.042087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0bc878fa2851'
down_revision: Union[str, None] = 'ba3859b8f107'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
