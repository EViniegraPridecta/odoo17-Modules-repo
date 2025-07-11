# Copyright 2020 ACSONE
# @author: Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Base EDI",
    "summary": """Base module to aggregate EDI features.""",
    "version": "17.0.1.1.1",
    "development_status": "Beta",
    "website": "https://github.com/OCA/edi",
    "license": "LGPL-3",
    "author": "ACSONE,Odoo Community Association (OCA)",
    "maintainers": ["simahawk"],
    "depends": ["base"],
    "data": [
        "data/module_category.xml",
        "security/edi_groups.xml",
        "views/edi_menu.xml",
    ],
}
