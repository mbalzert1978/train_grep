"""Bootstrap the application."""
import typing
from unittest.mock import MagicMock

import handler

if typing.TYPE_CHECKING:
    import types


def bootstrap(logger_type: str = "std_out") -> None:
    """
    Bootsstrap the application.

    Parameters
    ----------
    logger_type : str, optional
        _description_, by default "std_out"
    valid options:
        `std_out`, `file` or `none`

    """
    log_module: types.ModuleType
    match logger_type:
        case "std_out":
            log_module = handler.std_out_logger
        case "file":
            log_module = handler.file_logger
        case "none":
            log_module = MagicMock()
        case _:
            log_module = handler.std_out_logger

    log_module.setup()
    handler.parser.setup()
    handler.file_handler.setup()
    handler.finder.setup()
    handler.std_out_viewer.setup()
    handler.std_out_error_handler.setup()
