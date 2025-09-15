import shutil
from odoo import models, fields, api, _ # type: ignore
from odoo.exceptions import UserError # type: ignore

class ServerStatusWizard(models.TransientModel):
    _name = "server.status.wizard"
    _description = "Estado del Servidor"

    # --- Disco ---
    server_disk_path = fields.Char(string="Ruta de disco", default="/")
    server_total_space = fields.Char(string="Almacenamiento total", readonly=True)
    server_used_space = fields.Char(string="Espacio ocupado", readonly=True)
    server_free_space = fields.Char(string="Espacio libre", readonly=True)
    server_used_percent = fields.Char(string="% Usado", readonly=True)

    # --- Conteos de registros ---
    invoice_count = fields.Integer(string="Facturas", readonly=True)
    partner_count = fields.Integer(string="Contactos", readonly=True)
    product_count = fields.Integer(string="Productos", readonly=True)
    service_count = fields.Integer(string="Servicios", readonly=True)
    user_count = fields.Integer(string="Usuarios", readonly=True)

    @api.model
    def default_get(self, fields_list):
        """Al abrir el wizard, calcular estado de disco y conteos"""
        res = super().default_get(fields_list)

        # --- Estado del disco ---
        path = "/"
        try:
            total, used, free = shutil.disk_usage(path)
        except FileNotFoundError:
            raise UserError(_("La ruta '%s' no existe en el host/contenedor.") % path)

        total_gb = total / (2**30)
        used_gb = used / (2**30)
        free_gb = free / (2**30)
        used_pct = (used / total * 100) if total else 0

        res.update({
            "server_disk_path": path,
            "server_total_space": f"{total_gb/25:.1f} GB",
            "server_used_space": f"{used_gb/25:.1f} GB",
            "server_free_space": f"{free_gb/25:.1f} GB",
            "server_used_percent": f"{used_pct:.1f}%",
        })

        # --- Conteos ---
        res.update({
            "invoice_count": self.env["account.move"].search_count([
                ("move_type", "in", ("out_invoice", "in_invoice"))
            ]),
            "partner_count": self.env["res.partner"].search_count([]),
            "product_count": self.env["product.product"].search_count([]),
            "service_count": self.env["product.template"].search_count([
                ("detailed_type", "=", "service")
            ]),
            "user_count": self.env["res.users"].search_count([]),
        })

        return res
