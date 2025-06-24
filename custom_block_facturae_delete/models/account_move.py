from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def unlink(self):
        raise UserError(_("No está permitido eliminar facturas en ningún caso."))
