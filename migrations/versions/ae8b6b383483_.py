"""empty message

Revision ID: ae8b6b383483
Revises: d0116944645f
Create Date: 2022-07-29 13:39:10.011564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae8b6b383483'
down_revision = 'd0116944645f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###
