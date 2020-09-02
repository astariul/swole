import dominate


class Page():
    """ Class representing a page.

    Attributes:
        route (`str`): The route to access this page.
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

    def to_html(self):
        """ Method to get the `dominate` HTML of the page. This HTML needs to be
        rendered.

        Returns:
            dominate.document: HTML document corresponding to the page.
        """
        return dominate.document(title=self.title)
