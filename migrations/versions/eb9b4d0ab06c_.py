"""empty message

Revision ID: eb9b4d0ab06c
Revises: 
Create Date: 2019-12-17 17:48:00.168253

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils



# revision identifiers, used by Alembic.
revision = 'eb9b4d0ab06c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.Unicode(length=80), nullable=False),
    sa.Column('lastName', sa.Unicode(length=80), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.Boolean(), nullable=False),
    sa.Column('cnic', sa.String(length=13), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnic'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employee')
    # ### end Alembic commands ###
