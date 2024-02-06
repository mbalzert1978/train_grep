"""Custom Json logger https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/135_modern_logging/mylogger.py."""
import datetime as dt
import json
import logging
from collections.abc import Mapping
from typing import Any, Literal, override

LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}

_FormatStyle = Literal["%", "{", "$"]


class MyJSONFormatter(logging.Formatter):

    """Json Formater for logging."""

    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: _FormatStyle = "%",
        *,
        validate: bool = True,
        defaults: Mapping[str, Any] | None = None,
        fmt_keys: dict[str, str] | None = None,
    ) -> None:
        self.fmt_keys = fmt_keys or {}
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)

    @override
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord) -> dict[str, str]:
        always_fields = {
            "message": record.getMessage(),
            "timestamp": dt.datetime.fromtimestamp(record.created, tz=dt.UTC).isoformat(),
        }

        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: msg_val if (msg_val := always_fields.pop(val, None)) is not None else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }

        message |= always_fields

        for key, val in record.__dict__.items():
            if key in LOG_RECORD_BUILTIN_ATTRS:
                continue
            message[key] = val

        return message


class NonErrorFilter(logging.Filter):

    """Filter out non-error log records."""

    @override
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        return record.levelno <= logging.INFO
