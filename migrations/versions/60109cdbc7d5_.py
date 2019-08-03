"""empty message

Revision ID: 60109cdbc7d5
Revises: d732d9168604
Create Date: 2019-08-03 16:57:11.966193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60109cdbc7d5'
down_revision = 'd732d9168604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('sender', sa.String(length=64), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'receiver_id')
    )
    op.add_column('messages', sa.Column('receiver_id', sa.Integer(), nullable=False))
    op.add_column('messages', sa.Column('sender_id', sa.Integer(), nullable=False))
    op.drop_constraint('messages_user_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['receiver_id'], ['id'])
    op.create_foreign_key(None, 'messages', 'users', ['sender_id'], ['id'])
    op.drop_column('messages', 'sender')
    op.drop_column('messages', 'is_read')
    op.drop_column('messages', 'user_id')
    op.add_column('posts', sa.Column('draft', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'draft')
    op.add_column('messages', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('is_read', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('sender', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_user_id_fkey', 'messages', 'users', ['user_id'], ['id'])
    op.drop_column('messages', 'sender_id')
    op.drop_column('messages', 'receiver_id')
    op.drop_table('notifications')
    # ### end Alembic commands ###
