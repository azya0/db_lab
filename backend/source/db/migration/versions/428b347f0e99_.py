"""empty message

Revision ID: 428b347f0e99
Revises: 8a19592ca8c9
Create Date: 2024-04-26 21:41:27.095581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '428b347f0e99'
down_revision: Union[str, None] = '8a19592ca8c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('brigade', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('brigade', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('brigade', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('brigade', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###
