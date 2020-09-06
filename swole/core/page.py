import dominate

from swole.widgets.base import Widget


class Page():
    """ Class representing a page.

    Attributes:
        route (`str`): The route to access this page.
        skin (`str`): The name of the skin to use for this page.
        title (`str`): The title of the page.
    """
    def __init__(self, route="/", skin=None, title="Home"):
        """ Constructor.

        Arguments:
            route (`str`, optional): The route to access this page. Defaults to
                `/`.
            skin (`str`, optional): The name of the skin to use for this page.
                If `None`, base skin will be used. Defaults to `None`.
            title (`str`, optional): The title of the page. Defaults to `Home`.
        """
        self.route = route
        self.skin = skin
        self.title = title
        self.widgets = []

    def to_html(self):
        """ Method to get the `dominate` HTML of the page. This HTML needs to be
        rendered.

        Returns:
            dominate.document: HTML document corresponding to the page.
        """
        doc = dominate.document(title=self.title)
        for w in self.widgets:
            doc.add(w.to_html())
        return doc

    def add(self, widget):
        """ Method to add a widget to this page.

        Arguments:
            widget (`Widget`): Widget to add.
        """
        if not isinstance(widget, Widget):
            raise ValueError("The given argument is not a widget : {}".format(widget))

        self.widgets.append(widget)
