"""empty message

Revision ID: 20b2f2b029dd
Revises: 428b347f0e99
Create Date: 2024-04-26 21:45:45.587732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20b2f2b029dd'
down_revision: Union[str, None] = '428b347f0e99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('status_type', sa.Column('is_system_closed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('status_type', 'is_system_closed')
    # ### end Alembic commands ###
