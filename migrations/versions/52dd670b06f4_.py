"""empty message

Revision ID: 52dd670b06f4
Revises: 
Create Date: 2023-06-10 17:24:18.117980

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '52dd670b06f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###