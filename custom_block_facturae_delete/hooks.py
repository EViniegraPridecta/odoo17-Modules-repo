# hooks.py
from odoo import api, SUPERUSER_ID #type: ignore[import]

def post_init_hook(env):
    """Marcar como ever_posted todas las facturas ya validadas existentes."""
    cr = env.cr
    # crear un env con superusuario por si el hook se ejecuta sin él
    su_env = api.Environment(cr, SUPERUSER_ID, {})
    invoice_types = ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')
    su_env['account.move'].with_context(active_test=False).search([
        ('move_type', 'in', invoice_types),
        ('state', '=', 'posted'),
    ]).write({'ever_posted': True})
