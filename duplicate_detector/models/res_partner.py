from odoo import models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains("email", "phone")
    def _check_duplicate_contact(self):
        for partner in self:
            if not partner.email and not partner.phone:
                continue

            domain = [("id", "!=", partner.id)]

            if partner.email:
                domain_email = domain + [("email", "=", partner.email)]
                if self.search_count(domain_email):
                    raise ValidationError(
                        "Duplicate contact detected (same email)."
                    )

            if partner.phone:
                domain_phone = domain + [("phone", "=", partner.phone)]
                if self.search_count(domain_phone):
                    raise ValidationError(
                        "Duplicate contact detected (same phone)."
                    )
