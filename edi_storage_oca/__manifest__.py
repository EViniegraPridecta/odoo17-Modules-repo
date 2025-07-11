# Copyright 2020 ACSONE
# @author: Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "EDI Storage backend support",
    "summary": """
    Base module to allow exchanging files via storage backend (eg: SFTP).
    """,
    "version": "17.0.1.0.0",
    "development_status": "Beta",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/edi-framework",
    "author": "ACSONE,Odoo Community Association (OCA)",
    "depends": ["edi_oca", "fs_storage", "component"],
    "data": [
        "data/cron.xml",
        "data/job_channel_data.xml",
        "data/queue_job_function_data.xml",
        "security/ir_model_access.xml",
        "views/edi_backend_views.xml",
    ],
    "demo": ["demo/edi_backend_demo.xml"],
}
