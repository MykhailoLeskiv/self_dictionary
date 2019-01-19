"""empty message

Revision ID: 34c1db06c02c
Revises: 3cf3190e6d44
Create Date: 2019-01-06 12:11:11.088329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34c1db06c02c'
down_revision = '3cf3190e6d44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dictionary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('native_lang', sa.String(length=32), nullable=True),
    sa.Column('foreign_lang', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dictionary_foreign_lang'), 'dictionary', ['foreign_lang'], unique=False)
    op.create_index(op.f('ix_dictionary_native_lang'), 'dictionary', ['native_lang'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dictionary_native_lang'), table_name='dictionary')
    op.drop_index(op.f('ix_dictionary_foreign_lang'), table_name='dictionary')
    op.drop_table('dictionary')
    # ### end Alembic commands ###
