"""empty message

Revision ID: 8e125d2a4725
Revises: eb29af0339c6
Create Date: 2024-06-28 09:47:02.232888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e125d2a4725'
down_revision = 'eb29af0339c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amenities',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('countries',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('code', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('code'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('countries')
    op.drop_table('amenities')
    # ### end Alembic commands ###
