import typing

import model


class Handler:

    """Handler for a product."""

    product: model.Product

    def collect_events(self):
        while self.product.events:
            yield self.product.events.pop(0)

    def handle(self):
        raise NotImplementedError


class ArgumentHandler(Handler):

    """Handler for arguments."""

    product: model.Arguments

    def __init__(self, args: typing.Iterable) -> None:
        self.product = model.Arguments()
        super().__init__()

    def handle(self):
        self.product.parse_args(self.product.args)
