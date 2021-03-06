"""
Add creation date to User table.

Revision ID: 0cf50323c78b
Revises: 87fbbc224f10
Create Date: 2018-03-09 13:19:41.903196
"""

# revision identifiers, used by Alembic.
revision = "0cf50323c78b"
down_revision = "87fbbc224f10"

import sqlalchemy as sa


def upgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("creation_date", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###

    # ### population of test data ### #
    tester.populate_column("user", "creation_date", tester.TestDataType.DateTime)
    # ### end population of test data ### #


def downgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "creation_date")
    # ### end Alembic commands ###
