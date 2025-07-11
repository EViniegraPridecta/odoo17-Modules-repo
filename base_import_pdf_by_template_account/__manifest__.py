# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Import Pdf by Template Account",
    "version": "17.0.1.0.4",
    "website": "https://github.com/OCA/edi",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["account", "base_import_pdf_by_template"],
    "installable": True,
    "demo": [
        "demo/base_import_pdf_template.xml",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/base_import_pdf_template_views.xml",
    ],
    "maintainers": ["victoralmau"],
}
