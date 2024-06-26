"""empty message

Revision ID: 8a19592ca8c9
Revises: 
Create Date: 2024-04-24 03:24:29.360685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a19592ca8c9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('model', sa.String(length=128), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_car_id'), 'car', ['id'], unique=False)
    op.create_table('patient',
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('descriptions', sa.String(length=512), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('second_name', sa.String(length=64), nullable=False),
    sa.Column('patronymic', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patient_id'), 'patient', ['id'], unique=False)
    op.create_table('post',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('is_driver', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_id'), 'post', ['id'], unique=False)
    op.create_table('status_type',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_status_type_id'), 'status_type', ['id'], unique=False)
    op.create_table('call',
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_call_id'), 'call', ['id'], unique=False)
    op.create_table('worker',
    sa.Column('is_ill', sa.Boolean(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('second_name', sa.String(length=64), nullable=False),
    sa.Column('patronymic', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worker_id'), 'worker', ['id'], unique=False)
    op.create_table('brigade',
    sa.Column('call_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['call_id'], ['call.id'], ),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brigade_id'), 'brigade', ['id'], unique=False)
    op.create_table('brigade_xref_worker',
    sa.Column('brigade_id', sa.Integer(), nullable=False),
    sa.Column('worker_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brigade_id'], ['brigade.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['worker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brigade_xref_worker_id'), 'brigade_xref_worker', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_brigade_xref_worker_id'), table_name='brigade_xref_worker')
    op.drop_table('brigade_xref_worker')
    op.drop_index(op.f('ix_brigade_id'), table_name='brigade')
    op.drop_table('brigade')
    op.drop_index(op.f('ix_worker_id'), table_name='worker')
    op.drop_table('worker')
    op.drop_index(op.f('ix_call_id'), table_name='call')
    op.drop_table('call')
    op.drop_index(op.f('ix_status_type_id'), table_name='status_type')
    op.drop_table('status_type')
    op.drop_index(op.f('ix_post_id'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_patient_id'), table_name='patient')
    op.drop_table('patient')
    op.drop_index(op.f('ix_car_id'), table_name='car')
    op.drop_table('car')
    # ### end Alembic commands ###
