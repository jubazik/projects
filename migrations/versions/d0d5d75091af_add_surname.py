"""add surname

Revision ID: d0d5d75091af
Revises: f6eda7049057
Create Date: 2022-03-29 10:59:31.236845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0d5d75091af'
down_revision = 'f6eda7049057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author_model', sa.Column('surname', sa.String(length=64), server_default='Default', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author_model', 'surname')
    # ### end Alembic commands ###
