# Copyright 2012 - Now Savoir-faire Linux <https://www.savoirfairelinux.com/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class KPICategory(models.Model):
    """KPI Category."""

    _name = "kpi.category"
    _description = "KPI Category"
    name = fields.Char(required=True)
    description = fields.Text()
