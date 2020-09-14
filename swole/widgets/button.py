from dominate.tags import button

from swole.widgets.base import Widget


class Button(Widget):
    """ Widget to create a button.

    Attributes:
        text (`str`): Text of the button.
        primary (`bool`): Wether this button is primary or not.
    """
    def __init__(self, text="Button", primary=False, onclick=None):
        """ Constructor.

        Arguments:
            text (`str`, optional): Text of the button. Defaults to `Button`.
            primary (`bool`, optional): Wether this button is primary or not.
                Defaults to `False`.
            onclick (`Ajax`, optional): Ajax request to call if the button is
                clicked. If `None`, nothing happend on click. Defaults to
                `None`.
        """
        super().__init__()
        self.text = text
        self.primary = primary
        self.onclick = onclick

    def html(self):
        attributes = {"id": self.id}

        if self.primary:
            attributes["cls"] = "button-primary"

        if self.onclick is not None:
            attributes["onclick"] = "callback_{}()".format(self.onclick.id)

        return button(self.text, **attributes)

    def ajax(self):
        return self.onclick if self.onclick is not None else None
