"""Solitacao/NF

Revision ID: c31765b25b9f
Revises: fdaf5f3adf35
Create Date: 2024-04-23 20:38:20.653601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31765b25b9f'
down_revision = 'fdaf5f3adf35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solicitacao',
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('natureza', sa.String(length=1), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nota_fiscal',
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('emitente_id', sa.Integer(), nullable=True),
    sa.Column('remetente_id', sa.Integer(), nullable=True),
    sa.Column('solicitacao_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('natureza', sa.String(length=1), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['emitente_id'], ['pessoa_juridica.id'], ),
    sa.ForeignKeyConstraint(['remetente_id'], ['pessoa_juridica.id'], ),
    sa.ForeignKeyConstraint(['solicitacao_id'], ['solicitacao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solicitacao_produto',
    sa.Column('solicitacao_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.Column('qtde_solicitada', sa.Integer(), nullable=True),
    sa.Column('qtde_atendida', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.ForeignKeyConstraint(['solicitacao_id'], ['solicitacao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nota_fiscal_produto',
    sa.Column('nf_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.Column('qtde_solicitada', sa.Integer(), nullable=True),
    sa.Column('qtde_atendida', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['nf_id'], ['nota_fiscal.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nota_fiscal_produto')
    op.drop_table('solicitacao_produto')
    op.drop_table('nota_fiscal')
    op.drop_table('solicitacao')
    # ### end Alembic commands ###