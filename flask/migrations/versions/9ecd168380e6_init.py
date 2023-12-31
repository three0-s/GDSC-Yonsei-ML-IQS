"""init

Revision ID: 9ecd168380e6
Revises: 
Create Date: 2023-11-04 22:13:57.678492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ecd168380e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('common_questions_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cv_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.String(length=500), nullable=False),
    sa.Column('contents', sa.String(length=4096), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('cv_id', sa.Integer(), nullable=True),
    sa.Column('specific_question1', sa.String(length=512), nullable=True),
    sa.Column('specific_question2', sa.String(length=512), nullable=True),
    sa.Column('specific_question3', sa.String(length=512), nullable=True),
    sa.Column('specific_question4', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cv_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('cv_table')
    op.drop_table('common_questions_table')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
