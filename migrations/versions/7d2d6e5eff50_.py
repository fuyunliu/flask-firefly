"""empty message

Revision ID: 7d2d6e5eff50
Revises: 27c989070f01
Create Date: 2019-06-24 10:27:39.093277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d2d6e5eff50'
down_revision = '27c989070f01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('sender', sa.String(length=64), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tweets_create_time'), 'tweets', ['create_time'], unique=False)
    op.create_table('user_collect_post',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id', 'favorite_id')
    )
    op.create_table('user_like_tweet',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tweet_id')
    )
    op.add_column('comments', sa.Column('body_html', sa.Text(), nullable=True))
    op.add_column('comments', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('tweet_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_reply_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'tweets', ['tweet_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'comments', ['parent_id'], ['id'])
    op.drop_column('comments', 'reply_id')
    op.drop_column('comments', 'like_count')
    op.drop_column('posts', 'author_name')
    op.drop_column('posts', 'like_count')
    op.drop_column('user_like_comment', 'id')
    op.drop_column('user_like_post', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_like_post', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('user_like_comment', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('posts', sa.Column('like_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('author_name', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('like_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('reply_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_reply_id_fkey', 'comments', 'users', ['reply_id'], ['id'])
    op.drop_column('comments', 'tweet_id')
    op.drop_column('comments', 'parent_id')
    op.drop_column('comments', 'body_html')
    op.drop_table('user_like_tweet')
    op.drop_table('user_collect_post')
    op.drop_index(op.f('ix_tweets_create_time'), table_name='tweets')
    op.drop_table('tweets')
    op.drop_table('messages')
    op.drop_table('favorites')
    op.drop_table('topics')
    # ### end Alembic commands ###