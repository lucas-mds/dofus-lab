"""empty message

Revision ID: 285b17b32c4e
Revises: 138ae7ddca87
Create Date: 2020-03-04 22:48:06.172440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "285b17b32c4e"
down_revision = "138ae7ddca87"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "custom_set",
        "level",
        existing_type=sa.INTEGER(),
        nullable=False,
        server_default=sa.text("200"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("custom_set", "level", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###