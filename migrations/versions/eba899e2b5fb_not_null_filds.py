"""not null filds

Revision ID: eba899e2b5fb
Revises: 1214e9f404d4
Create Date: 2019-01-31 10:21:41.479063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eba899e2b5fb'
down_revision = '1214e9f404d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('chapter', 'chapter_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('dictionary', 'foreign_lang',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('dictionary', 'native_lang',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('word', 'translation',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('word', 'word',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('word', 'word',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('word', 'translation',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('dictionary', 'native_lang',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('dictionary', 'foreign_lang',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('chapter', 'chapter_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###
