"""empty message

Revision ID: d50af614a955
Revises: 404babea4938
Create Date: 2022-06-02 00:29:51.040070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50af614a955'
down_revision = '404babea4938'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
    op.create_foreign_key(op.f('fk_answer_user_id_user'), 'answer', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_question_user_id_user'), 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    op.create_unique_constraint(op.f('uq_user_username'), 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_username'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    op.drop_constraint(op.f('fk_question_user_id_user'), 'question', type_='foreignkey')
    op.drop_constraint(op.f('fk_answer_user_id_user'), 'answer', type_='foreignkey')
    op.drop_column('answer', 'user_id')
    # ### end Alembic commands ###