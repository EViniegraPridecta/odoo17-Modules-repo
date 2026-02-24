from odoo import models, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.constrains("name", "barcode")
    def _check_duplicate_product(self):
        for product in self:
            domain = [("id", "!=", product.id)]

            if product.barcode:
                if self.search_count(domain + [("barcode", "=", product.barcode)]):
                    raise ValidationError(
                        "Duplicate product barcode detected."
                    )

            if product.name:
                if self.search_count(domain + [("name", "=", product.name)]):
                    raise ValidationError(
                        "Duplicate product name detected."
                    )
