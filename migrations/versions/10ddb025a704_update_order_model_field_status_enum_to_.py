"""update order model field status enum to string

Revision ID: 10ddb025a704
Revises: 0bf92eccfb95
Create Date: 2025-03-19 20:16:45.562840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10ddb025a704'
down_revision = '0bf92eccfb95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=9),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('tracking_code',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('tracking_code',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=9),
               existing_nullable=True)

    # ### end Alembic commands ###
