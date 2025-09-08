# -*- coding: utf-8 -*-
from odoo import api, fields, models, _ #type:ignore[import-error]
from odoo.exceptions import UserError #type:ignore[import-error]

INVOICE_TYPES = ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Marcador permanente: si se publica una vez, queda True para siempre.
    ever_posted = fields.Boolean(
        string='Ever Posted',
        default=False,
        copy=False,
        index=True
    )

    # 1) Asegurar que al validar quede marcado
    def action_post(self):
        res = super().action_post()
        # Marcar sólo documentos de tipo factura/recibo (no asientos generales)
        to_mark = self.filtered(lambda m: m.move_type in INVOICE_TYPES)
        if to_mark:
            to_mark.write({'ever_posted': True})
        return res

    # 2) Impedir que alguien (incluso admin) baje el flag
    def write(self, vals):
        if 'ever_posted' in vals:
            # No permitir pasar de True -> False jamás
            if any(rec.ever_posted for rec in self) and not vals.get('ever_posted'):
                raise UserError(_("No está permitido desactivar 'ever_posted'."))
        return super().write(vals)

    # 3) Bloquear el unlink de por vida cuando ever_posted=True
    @api.ondelete(at_uninstall=False)
    def _no_delete_if_ever_posted(self):
        bad = self.filtered(lambda m: m.move_type in INVOICE_TYPES and m.ever_posted)
        if bad:
            # Mensaje único y claro; mostrar números para auditoría
            raise UserError(_(
                "No se pueden eliminar las siguientes facturas/notas/recibos porque "
                "han sido validados alguna vez:\n%s"
            ) % "\n".join(bad.mapped('name') or ['(sin número)']))
