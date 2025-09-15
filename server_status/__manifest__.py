{
    "name": "Server Status",
    "version": "17.0.2.0.1",
    "author": "Esteban Viniegra | Pridecta",
    "website": "https://pridecta.es",
    "license": "LGPL-3",
    "category": "Administration",
    "summary": "Muestra el estado de almacenamiento del servidor en Ajustes",
    "depends": ["base_setup"],  # <- importante en Odoo 17
    "data": [
        "security/ir.model.access.csv",
        "views/server_status_wizard_view.xml",
        "views/about_wizard_view.xml",
        "views/res_config_settings_view.xml",
    ],
    "icon": "/server_status/static/description/icon.png",
    "application": False,
    "installable": True,
}
