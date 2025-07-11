# Copyright 2020 ACSONE
# @author: Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo.addons.component.core import Component

from .. import utils


class EDIStorageSendComponent(Component):
    _name = "edi.storage.component.send"
    _inherit = [
        "edi.component.send.mixin",
        "edi.storage.component.mixin",
    ]
    _usage = "storage.send"

    def send(self):
        # If the file has been sent already, refresh its state
        # TODO: double check if this is useless
        # since the backend checks the state already
        checker = self.component(usage="storage.check")
        result = checker.check()
        if not result:
            # all good here
            return True
        filedata = self.exchange_record.exchange_file
        path = self._get_remote_file_path("pending")
        utils.add_file(self.storage, path.as_posix(), filedata)
        # TODO: delegate this to generic storage backend
        # except paramiko.ssh_exception.AuthenticationException:
        #     # TODO this exc handling should be moved to sftp backend IMO
        #     error = _("Authentication error")
        #     state = "error_on_send"
        # TODO: catch other specific exceptions
        # this will swallow all the exceptions!
        return True
