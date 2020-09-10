import dominate
from dominate.tags import script

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

    def html(self):
        """ Method to get the `dominate` HTML of the page. This HTML needs to be
        rendered.

        Returns:
            dominate.document: HTML document corresponding to the page.
        """
        doc = dominate.document(title=self.title)

        # Add Widgets HTML to the page
        for w in self.widgets:
            doc.add(w.html())

        # Add Javascript code to the page
        js = [w.js() for w in self.widgets]
        js_str = "\n\n".join([s for s in js if s is not None])
        if js_str != '':
            doc.add(script(js_str))

        return doc

    def add(self, widget):
        """ Method to add a widget to this page.

        Arguments:
            widget (`Widget`): Widget to add.
        """
        if not isinstance(widget, Widget):
            raise ValueError("The given argument is not a widget : {}".format(widget))

        self.widgets.append(widget)
