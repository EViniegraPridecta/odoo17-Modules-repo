# Copyright 2020 ACSONE
# Copyright 2022 Camptocamp
# @author: Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import logging
from pathlib import PurePath

from odoo.addons.component.core import AbstractComponent

from .. import utils

_logger = logging.getLogger(__file__)


class EDIStorageComponentMixin(AbstractComponent):
    _name = "edi.storage.component.mixin"
    _inherit = "edi.component.mixin"
    # Components having `_storage_type` will have precedence.
    # If the value is not set, generic components will be used.
    _storage_type = None

    @classmethod
    def _component_match(cls, work, usage=None, model_name=None, **kw):
        res = super()._component_match(work, usage=usage, model_name=model_name, **kw)
        storage_type = kw.get("storage_type")
        if storage_type and cls._storage_type:
            return cls._storage_type == storage_type
        return res

    @property
    def storage(self):
        return self.backend.storage_id

    def _dir_by_state(self, direction, state):
        """Return remote directory path by direction and state.

        :param direction: string stating direction of the exchange
        :param state: string stating state of the exchange
        :return: PurePath object
        """
        assert direction in ("input", "output")
        assert state in ("pending", "done", "error")
        return PurePath(
            (self.backend[direction + "_dir_" + state] or "").strip().rstrip("/")
        )

    def _get_remote_file_path(self, state, filename=None):
        """Retrieve remote path for current exchange record."""
        filename = filename or self.exchange_record.exchange_filename
        direction = self.exchange_record.direction
        directory = self._dir_by_state(direction, state).as_posix()
        path = self.exchange_record.type_id._storage_fullpath(
            directory=directory, filename=filename
        )
        return path

    def _get_remote_file(self, state, filename=None, binary=False):
        """Get file for current exchange_record in the given destination state.

        :param state: string ("pending", "done", "error")
        :param filename: custom file name, exchange_record filename used by default
        :return: remote file content as string
        """
        path = self._get_remote_file_path(state, filename=filename)
        try:
            # TODO: support match via pattern (eg: filename-prefix-*)
            # otherwise is impossible to retrieve input files and acks
            # (the date will never match)
            return utils.get_file(self.storage, path.as_posix(), binary=binary)
        except FileNotFoundError:
            _logger.info(
                "Ignored FileNotFoundError when trying "
                "to get file %s into path %s for state %s",
                filename,
                path,
                state,
            )
            return None
        except OSError:
            _logger.info(
                "Ignored OSError when trying to get file %s into path %s for state %s",
                filename,
                path,
                state,
            )
            return None
