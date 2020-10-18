from dominate.tags import h1, h2, h3, h4, h5, h6

from swole.widgets.base import Widget


H_X = [h1, h2, h3, h4, h5, h6]


class Header(Widget):
    """ Widget to create a header.

    Attributes:
        text (`str`): Text of the header.
        level (`int`): Leve of the header. `1` to `6` only.
        center (`bool`): Wether to put this header in the middle.
    """
    def __init__(self, text="Header", level=2, center=False, **kwargs):
        """ Constructor.

        Arguments:
            text (`str`, optional): Text of the header. Defaults to `Header`.
            level(`int`, optional): Level of the header. Defaults to `2`.
            center (`bool`, optional): Wether to put this header in the middle
                or not. Defaults to `False`.
        """
        if level not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Header should be an `int` between 1 and 6")

        super().__init__(**kwargs)
        self.text = text
        self.level = level - 1

        if center:
            self.cls.insert(0, "center")

    def html(self):
        attributes = {"id": self.id}
        self.add_css_class(attributes)

        return H_X[self.level](self.text, **attributes)

    def get(self):
        return self.text

    def set(self, x):
        self.text = x


class Title(Header):
    """ Widget to create a title. A title is a Header with level 1. """
    def __init__(self, *args, **kwargs):
        """ Constructor. """
        super().__init__(*args, level=1, **kwargs)


class SubHeader(Header):
    """ Widget to create a sub-header. A sub-header is a Header with level 3. """
    def __init__(self, *args, **kwargs):
        """ Constructor. """
        super().__init__(*args, level=3, **kwargs)