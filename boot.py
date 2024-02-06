"""Bootstrap the application."""
import handler


def bootstrap() -> None:
    """Set up the handler."""
    handler.std_out_logger.setup()
    handler.parser.setup()
    handler.file_handler.setup()
    handler.finder.setup()
    handler.std_out_viewer.setup()
    handler.std_out_error_handler.setup()
