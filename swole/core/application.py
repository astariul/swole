from swole.core.page import Page


class Application():
    """ Class representing an application. An application is the englobing,
    object, which list all possible routes.

    Attributes:
        pages (`dict`): Dictionary[`str`: `Page`] listing all possible routes
            and their corresponding Page.
    """
    def __init__(self, pages=None):
        """ Constructor.

        Arguments:
            pages (`dict`, optional): Dictionary[`str`: `Page`] listing routes
                and their corresponding Page. If `None` is given, it
                automatically create a page for the route `/`. Defaults to
                `None`.
        """
        if pages is None:
            self.pages = {'/': Page()}
        else:
            self.pages = {p.route: p for p in pages}

    def add(self, pages):
        """ Method to add pages to the application.

        Arguments:
            pages (`Page` or `list`): Page or list of Page to add.
        """
        if isinstance(pages, list):
            for page in pages:
                self._add(page)
        else:
            self._add(pages)

    def _add(self, page):
        if not isinstance(page, Page):
            raise ValueError("Expected a Page type, got a {} type instead".format(type(page)))

        if page.route in self.pages:
            raise ValueError("This route ({}) is already set".format(page.route))

        self.pages[page.route] = page
