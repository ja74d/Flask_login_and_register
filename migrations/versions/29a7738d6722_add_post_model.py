"""add post model

Revision ID: 29a7738d6722
Revises: 
Create Date: 2022-01-20 11:06:42.805753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a7738d6722'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
