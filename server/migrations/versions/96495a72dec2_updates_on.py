"""updates on ...

Revision ID: 96495a72dec2
Revises: 4cb64ab212f4
Create Date: 2024-01-22 02:18:33.661019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96495a72dec2'
down_revision = '4cb64ab212f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizza', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizza', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)

    # ### end Alembic commands ###
