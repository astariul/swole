from dominate.tags import input_

from swole.widgets.base import WideWidget, labeled


@labeled
class Input(WideWidget):
    """ Widget to create an input. """
    def __init__(self, type="number", placeholder=None, wide=True, **kwargs):
        """
        Arguments:
            type (`str`, optional): Type of the input. Defaults to `number`.
            placeholder (`str`, placeholder): Placeholder for the input. If
                `None`, no placeholder is used. Defaults to `None`.
        """
        super().__init__(wide=wide, **kwargs)
        self.type = type
        self.placeholder = placeholder
        self.value = placeholder
        self.jquery_fn = "val"

    def html(self):
        attributes = {
            "id": self.id,
            "type": self.type,
        }
        self.add_css_class(attributes)

        if self.placeholder is not None:
            attributes["placeholder"] = self.placeholder

        return input_(**attributes)

    def get(self):
        return self.value

    def set(self, x):
        if self.type == "number" and isinstance(x, str):
            try:
                # Find if it's an int or a float
                number = float(x)
                integer = int(number)
                # number, integer = float(x), int(x)
                self.value = integer if number == integer else number
            except ValueError:      # Empty input
                self.value = 0
        else:
            self.value = x
