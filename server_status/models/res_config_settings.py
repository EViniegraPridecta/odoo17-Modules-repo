import shutil
from odoo import models, fields, api, _ #type: ignore
from odoo.exceptions import UserError #type: ignore

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    server_total_space = fields.Char(
        string="Almacenamiento total", readonly=True, compute="_compute_server_status"
    )
    server_used_space = fields.Char(
        string="Espacio ocupado", readonly=True, compute="_compute_server_status"
    )
    server_free_space = fields.Char(
        string="Espacio libre", readonly=True, compute="_compute_server_status"
    )
    server_used_percent = fields.Char(
        string="% Usado", readonly=True, compute="_compute_server_status"
    )

    # Ruta configurable (se guarda en ir.config_parameter)
    server_disk_path = fields.Char(
        string="Ruta de disco a monitorear",
        config_parameter="server_status.disk_path",
        default="/",
        help="Ruta del filesystem cuya capacidad se desea medir. "
             "Ej.: '/', '/host', '/var/lib/odoo', etc."
    )

    @api.model
    def _get_disk_usage(self, path: str):
        """Devuelve métricas de disco para la ruta dada, en GB (1 decimal) y % usado."""
        try:
            total, used, free = shutil.disk_usage(path)
        except FileNotFoundError:
            raise UserError(_("La ruta '%s' no existe en el contenedor/host.") % path)
        except PermissionError:
            raise UserError(_("No hay permisos para acceder a la ruta '%s'.") % path)

        total_gb = total / (2**30)
        used_gb = used / (2**30)
        free_gb = free / (2**30)
        used_pct = (used / total * 100) if total else 0.0

        return {
            "total": f"{total_gb:.1f} GB",
            "used": f"{used_gb:.1f} GB",
            "free": f"{free_gb:.1f} GB",
            "percent": f"{used_pct:.1f}%",
        }

    @api.depends("server_disk_path")
    def _compute_server_status(self):
        """Compute centralizado: llena total/used/free/% según la ruta configurada."""
        for rec in self:
            path = rec.server_disk_path or "/"
            try:
                status = self._get_disk_usage(path)
            except UserError:
                rec.server_total_space = "N/D"
                rec.server_used_space = "N/D"
                rec.server_free_space = "N/D"
                rec.server_used_percent = "N/D"
                continue

            rec.server_total_space = status["total"]
            rec.server_used_space = status["used"]
            rec.server_free_space = status["free"]
            rec.server_used_percent = status["percent"]

    def action_check_server_status(self):
        """Botón: recalcula y muestra notificación."""
        self._compute_server_status()
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Estado del Servidor"),
                "message": _(
                    "Ruta: %s\nTotal: %s | Ocupado: %s (%s) | Libre: %s"
                ) % (
                    self.server_disk_path or "/",
                    self.server_total_space,
                    self.server_used_space,
                    self.server_used_percent,
                    self.server_free_space,
                ),
                "sticky": False,
            },
        }
