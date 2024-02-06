"""Bootstrap the application."""
import handler


def bootstrap() -> None:
    """Bootstrap the application."""
    handler.logger.setup()
    handler.args.setup()
    handler.file.setup()
    handler.lines.setup()
    handler.std_out.setup()
    handler.std_err.setup()
