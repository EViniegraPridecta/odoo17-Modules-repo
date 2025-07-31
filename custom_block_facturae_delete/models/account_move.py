from odoo import models, _ # type: ignore[import]
from odoo.exceptions import UserError # type: ignore[import]

class AccountMove(models.Model):
    _inherit = 'account.move'

    def unlink(self):
        # Permitir solo durante instalación o actualización de módulos
        if self.env.context.get('install_mode') or self.env.context.get('upgrade_mode'):
            return super().unlink()

        raise UserError(_("No está permitido eliminar facturas. Si necesita anular una factura, utilice la opción de anulación."))
