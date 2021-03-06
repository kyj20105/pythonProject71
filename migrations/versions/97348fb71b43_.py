"""empty message

Revision ID: 97348fb71b43
Revises: d50af614a955
Create Date: 2022-06-05 19:58:03.768802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97348fb71b43'
down_revision = 'd50af614a955'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('modify_date', sa.DateTime(), nullable=True))
    op.create_foreign_key(op.f('fk_answer_user_id_user'), 'answer', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('question', sa.Column('modify_date', sa.DateTime(), nullable=True))
    op.create_foreign_key(op.f('fk_question_user_id_user'), 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    op.create_unique_constraint(op.f('uq_user_username'), 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_username'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    op.drop_constraint(op.f('fk_question_user_id_user'), 'question', type_='foreignkey')
    op.drop_column('question', 'modify_date')
    op.drop_constraint(op.f('fk_answer_user_id_user'), 'answer', type_='foreignkey')
    op.drop_column('answer', 'modify_date')
    # ### end Alembic commands ###
