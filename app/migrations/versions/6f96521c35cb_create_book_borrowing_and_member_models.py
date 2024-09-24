"""create Book,Borrowing and Member models

Revision ID: 6f96521c35cb
Revises: 
Create Date: 2024-09-24 14:39:13.280878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '6f96521c35cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'members',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'books',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('author', sa.String(), nullable=False)
    )

    op.create_table(
        'borrowings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('member_id', sa.Integer(), sa.ForeignKey('members.id'), nullable=False),
        sa.Column('book_id', sa.Integer(), sa.ForeignKey('books.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('borrowings')
    op.drop_table('books')
    op.drop_table('members')
