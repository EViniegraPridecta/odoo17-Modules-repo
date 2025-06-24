from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def write(self, vals):
        for move in self:
            # Si intenta regresar a borrador
            if vals.get('state') == 'draft':
                if move.move_type in ['out_invoice', 'out_refund'] and move.facturae and move.facturae_file_reference:
                    raise UserError(_("No se puede regresar a borrador una factura que ha sido firmada con Facturae."))
        return super().write(vals)

    def unlink(self):
        for move in self:
            if move.move_type in ['out_invoice', 'out_refund'] and move.facturae and move.facturae_file_reference:
                raise UserError(_("No se puede eliminar una factura que ha sido firmada con Facturae."))
        return super().unlink()

