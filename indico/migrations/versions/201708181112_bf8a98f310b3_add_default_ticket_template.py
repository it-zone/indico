"""Add default ticket template

Revision ID: bf8a98f310b3
Revises: aecc0b2792bb
Create Date: 2017-08-18 11:12:35.662385
"""

import json

import sqlalchemy as sa
from alembic import op

from indico.core.db.sqlalchemy.util.management import DEFAULT_TEMPLATE_DATA
from indico.modules.designer import TemplateType


# revision identifiers, used by Alembic.
revision = 'bf8a98f310b3'
down_revision = 'aecc0b2792bb'
branch_labels = None
depends_on = None


def upgrade():
    stmt = sa.text('''
        INSERT INTO indico.designer_templates
            (category_id, title, type, data, is_system_template, is_clonable)
        VALUES
            (:category_id, :title, :type, :data, true, true)
    ''')
    op.execute(stmt.bindparams(category_id=0, title='Default ticket', type=TemplateType.badge.value,
                               data=json.dumps(DEFAULT_TEMPLATE_DATA)))


def downgrade():
    pass