"""empty message

Revision ID: 532a490e07d0
Revises: None
Create Date: 2016-06-06 01:07:26.459738

"""

# revision identifiers, used by Alembic.
revision = '532a490e07d0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    pass
    ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('note')
    ### end Alembic commands ###


def downgrade():
    pass
    ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('note',
    # sa.Column('id', sa.INTEGER(), nullable=False),
    # sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('user_book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.ForeignKeyConstraint(['user_book_id'], [u'red_user_books.id'], name=u'note_user_book_id_fkey'),
    # sa.PrimaryKeyConstraint('id', name=u'note_pkey')
    # )
    ### end Alembic commands ###
