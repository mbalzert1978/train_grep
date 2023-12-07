"""Bootstrap the application."""
import collector
import error
import finder
import parsing
import stdout_logger
import view


def bootstrap() -> None:
    """Set up the handler."""
    stdout_logger.setup()
    parsing.setup()
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()
