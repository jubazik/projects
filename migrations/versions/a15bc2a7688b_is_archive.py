"""is_archive

Revision ID: a15bc2a7688b
Revises: 9acef237f597
Create Date: 2022-04-07 09:49:44.586241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a15bc2a7688b'
down_revision = '9acef237f597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_model', sa.Column('is_archive', sa.Boolean(), server_default=sa.text('0'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note_model', 'is_archive')
    # ### end Alembic commands ###
