"""Bootstrap the application."""
import collector
import error
import finder
import parsing
import stout_logger
import view


def bootstrap() -> None:
    """Set up the handler."""
    stout_logger.setup()
    parsing.setup()
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()
