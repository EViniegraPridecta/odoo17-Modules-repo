# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Punto de venta adaptado a la legislación española",
    "category": "Sales/Point Of Sale",
    "author": "Tecnativa, "
    "Aselcis Consulting, "
    "Acysos S.L., "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "depends": ["point_of_sale", "l10n_es"],
    "data": ["views/pos_views.xml", "views/res_config_settings_views.xml"],
    "assets": {
        "point_of_sale._assets_pos": [
            "l10n_es_pos_oca/static/src/**/*",
        ],
    },
    "installable": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
