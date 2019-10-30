"""empty message

Revision ID: 50baf778c3ab
Revises: 
Create Date: 2018-05-18 10:48:55.545757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50baf778c3ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_seenlist',
    sa.Column('myseenlist_id', sa.Integer(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=True),
    sa.Column('tv', sa.Text(), nullable=True),
    sa.Column('theater', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['director.director_id'], ),
    sa.PrimaryKeyConstraint('myseenlist_id'),
    sa.UniqueConstraint('myseenlist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_seenlist')
    # ### end Alembic commands ###