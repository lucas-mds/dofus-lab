"""empty message

Revision ID: ba9a71425f36
Revises: 138ae7ddca87
Create Date: 2020-03-04 17:17:31.776338

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ba9a71425f36'
down_revision = '138ae7ddca87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('set_translation',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('set_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('locale', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['set_id'], ['set.uuid'], name=op.f('fk_set_translation_set_id_set')),
    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_set_translation'))
    )
    op.create_table('item_translation',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('item_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('locale', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.uuid'], name=op.f('fk_item_translation_item_id_item')),
    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_item_translation'))
    )
    op.add_column('item', sa.Column('dofus_db_id', sa.String(), nullable=False))
    op.drop_column('item', 'name')
    op.add_column('item_stat', sa.Column('alt_stat', sa.String(), nullable=True))
    op.add_column('set', sa.Column('dofus_db_id', sa.String(), nullable=False))
    op.drop_column('set', 'name')
    op.add_column('set_bonus', sa.Column('alt_stat', sa.String(), nullable=True))
    op.alter_column('set_bonus', 'max_value',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('set_bonus', 'stat',
               existing_type=postgresql.ENUM('VITALITY', 'AP', 'MP', 'INITIATIVE', 'PROSPECTING', 'RANGE', 'SUMMON', 'WISDOM', 'STRENGTH', 'INTELLIGENCE', 'CHANCE', 'AGILITY', 'AP_PARRY', 'AP_REDUCTION', 'MP_PARRY', 'MP_REDUCTION', 'CRITICAL', 'HEALS', 'LOCK', 'DODGE', 'PCT_FINAL_DAMAGE', 'POWER', 'CRITICAL_DAMAGE', 'NEUTRAL_DAMAGE', 'EARTH_DAMAGE', 'FIRE_DAMAGE', 'WATER_DAMAGE', 'AIR_DAMAGE', 'REFLECT', 'TRAP_DAMAGE', 'TRAP_POWER', 'PUSHBACK_DAMAGE', 'PCT_SPELL_DAMAGE', 'PCT_WEAPON_DAMAGE', 'PCT_RANGED_DAMAGE', 'PCT_MELEE_DAMAGE', 'NEUTRAL_RES', 'PCT_NEUTRAL_RES', 'EARTH_RES', 'PCT_EARTH_RES', 'FIRE_RES', 'PCT_FIRE_RES', 'WATER_RES', 'PCT_WATER_RES', 'AIR_RES', 'PCT_AIR_RES', 'CRITICAL_RES', 'PUSHBACK_RES', 'PCT_RANGED_RES', 'PCT_MELEE_RES', name='stat'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('set_bonus', 'stat',
               existing_type=postgresql.ENUM('VITALITY', 'AP', 'MP', 'INITIATIVE', 'PROSPECTING', 'RANGE', 'SUMMON', 'WISDOM', 'STRENGTH', 'INTELLIGENCE', 'CHANCE', 'AGILITY', 'AP_PARRY', 'AP_REDUCTION', 'MP_PARRY', 'MP_REDUCTION', 'CRITICAL', 'HEALS', 'LOCK', 'DODGE', 'PCT_FINAL_DAMAGE', 'POWER', 'CRITICAL_DAMAGE', 'NEUTRAL_DAMAGE', 'EARTH_DAMAGE', 'FIRE_DAMAGE', 'WATER_DAMAGE', 'AIR_DAMAGE', 'REFLECT', 'TRAP_DAMAGE', 'TRAP_POWER', 'PUSHBACK_DAMAGE', 'PCT_SPELL_DAMAGE', 'PCT_WEAPON_DAMAGE', 'PCT_RANGED_DAMAGE', 'PCT_MELEE_DAMAGE', 'NEUTRAL_RES', 'PCT_NEUTRAL_RES', 'EARTH_RES', 'PCT_EARTH_RES', 'FIRE_RES', 'PCT_FIRE_RES', 'WATER_RES', 'PCT_WATER_RES', 'AIR_RES', 'PCT_AIR_RES', 'CRITICAL_RES', 'PUSHBACK_RES', 'PCT_RANGED_RES', 'PCT_MELEE_RES', name='stat'),
               nullable=False)
    op.alter_column('set_bonus', 'max_value',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('set_bonus', 'alt_stat')
    op.add_column('set', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('set', 'dofus_db_id')
    op.drop_column('item_stat', 'alt_stat')
    op.add_column('item', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('item', 'dofus_db_id')
    op.drop_table('item_translation')
    op.drop_table('set_translation')
    # ### end Alembic commands ###