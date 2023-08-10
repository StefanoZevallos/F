"""creacion de tabla usuarios

Revision ID: 5ed2d38ed0e7
Revises: 
Create Date: 2023-08-08 15:08:52.309091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed2d38ed0e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('apellido', sa.Text(), nullable=False),
    sa.Column('correo', sa.Text(), nullable=False),
    sa.Column('telefono', sa.Text(), nullable=True),
    sa.Column('linkedin_url', sa.Text(), nullable=True),
    sa.Column('direccion', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
