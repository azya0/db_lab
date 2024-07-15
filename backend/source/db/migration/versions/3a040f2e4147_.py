"""empty message

Revision ID: 3a040f2e4147
Revises: d151242db5e6
Create Date: 2024-05-23 11:06:04.243217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a040f2e4147'
down_revision: Union[str, None] = 'd151242db5e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('test_model_1000_fake_unique_key', 'test_model_1000', type_='unique')
    op.drop_constraint('test_model_10000_fake_unique_key', 'test_model_10000', type_='unique')
    op.drop_constraint('test_model_100000_fake_unique_key', 'test_model_100000', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('test_model_100000_fake_unique_key', 'test_model_100000', ['fake_unique'])
    op.create_unique_constraint('test_model_10000_fake_unique_key', 'test_model_10000', ['fake_unique'])
    op.create_unique_constraint('test_model_1000_fake_unique_key', 'test_model_1000', ['fake_unique'])
    # ### end Alembic commands ###