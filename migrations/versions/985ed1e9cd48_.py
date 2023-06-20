"""empty message

Revision ID: 985ed1e9cd48
Revises: 52dd670b06f4
Create Date: 2023-06-13 19:13:43.695246

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '985ed1e9cd48'
down_revision = '52dd670b06f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('u', ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('u', type_='unique')

    # ### end Alembic commands ###
