from dominate.tags import button

from swole.widgets.base import Widget


class Button(Widget):
    """ Widget to create a button. 

    Attributes:
        text (`str`): Text of the button.
        primary (`bool`): Wether this button is primary or not.
    """
    def __init__(self, text="Button", primary=False):
        """ Constructor.
        
        Arguments:
            text (`str`, optional): Text of the button. Defaults to `Button`.
            primary (`bool`, optional): Wether this button is primary or not.
                Defaults to `False`.
        """
        super().__init__()
        self.text = text
        self.primary = primary

    def to_html(self):
        attributes = {}

        if self.primary:
            attributes["cls"] = "button-primary"

        return button(self.text, **attributes)

