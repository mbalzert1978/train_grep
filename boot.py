"""Bootstrap the application."""
import arg_parser
import collector
import error
import finder
import stout_logger
import view


def bootstrap() -> None:
    """Set up the handler."""
    stout_logger.setup()
    arg_parser.setup()
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()
