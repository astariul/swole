from dominate.tags import input_

from swole.widgets.base import Widget


class Input(Widget):
    """ Widget to create an input.

    Attributes:
        type (`str`): Type of input.
        placeholder (`str`): Placeholder of input.
    """
    def __init__(self, type="number", placeholder=None):
        """ Constructor.

        Arguments:
            type (`str`, optional): Type of the input. Defaults to `number`.
            placeholder (`str`, placeholder): Placeholder for the input. If
                `None`, no placeholder is used. Defaults to `None`.
        """
        super().__init__()
        self.type = type
        self.placeholder = placeholder

    def to_html(self):
        attributes = {
            "id": self.id,
            "type": self.type,
        }

        if self.placeholder is not None:
            attributes["placeholder"] = self.placeholder

        return input_(**attributes)
