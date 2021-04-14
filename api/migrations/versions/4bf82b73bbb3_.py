"""empty message

Revision ID: 4bf82b73bbb3
Revises: 13f777964cf9
Create Date: 2021-03-29 15:32:40.197221

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utc


# revision identifiers, used by Alembic.
revision = '4bf82b73bbb3'
down_revision = '13f777964cf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('citizen', sa.Column('created_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=True))
    op.add_column('office', sa.Column('currently_waiting', sa.Integer(), nullable=True))
    op.add_column('office', sa.Column('digital_signage_message', sa.Integer(), nullable=True))
    op.add_column('office', sa.Column('digital_signage_message_1', sa.Text(), nullable=True))
    op.add_column('office', sa.Column('digital_signage_message_2', sa.Text(), nullable=True))
    op.add_column('office', sa.Column('digital_signage_message_3', sa.Text(), nullable=True))
    op.add_column('office', sa.Column('show_currently_waiting_bottom', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('office', 'show_currently_waiting_bottom')
    op.drop_column('office', 'digital_signage_message_3')
    op.drop_column('office', 'digital_signage_message_2')
    op.drop_column('office', 'digital_signage_message_1')
    op.drop_column('office', 'digital_signage_message')
    op.drop_column('office', 'currently_waiting')
    op.drop_column('citizen', 'created_at')
    # ### end Alembic commands ###