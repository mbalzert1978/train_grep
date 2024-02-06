"""Bootstrap the application."""
import handler


def bootstrap() -> None:
    """Bootstrap the application."""
    handler.std_out_logger.setup()
    handler.parser.setup()
    handler.file_handler.setup()
    handler.finder.setup()
    handler.std_out_viewer.setup()
    handler.std_out_error_handler.setup()
