"""empty message

Revision ID: 4dcb947d66af
Revises: 8e9f0f35cbcf
Create Date: 2024-05-16 03:00:43.959297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dcb947d66af'
down_revision: Union[str, None] = '8e9f0f35cbcf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worker', sa.Column('is_fired', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('worker', 'is_fired')
    # ### end Alembic commands ###