"""empty message

Revision ID: d6e9fda611e6
Revises: 
Create Date: 2019-09-01 16:10:45.462960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e9fda611e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('subject', sa.String(length=128), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    # ### end Alembic commands ###
