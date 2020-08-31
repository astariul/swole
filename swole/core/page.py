class Page():
    """ Class representing a page.

    Attributes:
        route (`str`): The route to access this page.
    """
    def __init__(self, route="/"):
        """ Constructor.

        Arguments:
            route (`str`, optional): The route to access this page. Defaults to
                `/`.
        """
        self.route = route
