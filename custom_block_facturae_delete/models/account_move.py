from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def unlink(self):
        raise UserError(_("No está permitido eliminar facturas. Si necesita anular una factura, utilice la opción de anulación."))