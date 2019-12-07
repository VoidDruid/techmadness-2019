"""


Revision ID: 7bd79b16bd4f
Revises: fc0d0df8c0cf
Create Date: 2019-12-07 06:10:50.000918

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bd79b16bd4f'
down_revision = 'fc0d0df8c0cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offers',
    sa.Column('offer_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('offer_template_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['offer_template_id'], ['offer_templates.offer_template_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('offer_id')
    )
    op.create_index(op.f('ix_offers_offer_id'), 'offers', ['offer_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_offers_offer_id'), table_name='offers')
    op.drop_table('offers')
    # ### end Alembic commands ###
