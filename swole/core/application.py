import os

from fastapi import FastAPI
from starlette.responses import FileResponse
import uvicorn

from swole.core.page import Page
from swole.core.utils import route_to_filename


SWOLE_CACHE = "~/.cache/swole"


class Application():
    """ Class representing an application. An application is the englobing,
    object, which list all possible routes.

    Attributes:
        pages (`dict`): Dictionary[`str`: `Page`] listing all possible routes
            and their corresponding Page.
        files (`dict`): Dictionary[`str`: `str`] listing all possible routes and
            their corresponding saved HTML file. This attribute is set only
            after calling the method `write()`.
        fapi (`fastapi.FastAPI`): FastAPI app.
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
        self.files = None
        self.fapi = FastAPI()

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

    def write(self, folder=SWOLE_CACHE):
        """ Method to write the HTML of the application to files, in order to
        later serve it.

        Arguments:
            folder (`str`, optional): Folder where to save HTML files. Defaults
                to SWOLE_CACHE.
        """
        os.makedirs(folder, exist_ok=True)

        self.files = {}
        for route, page in self.pages.items():
            html_str = page.to_html().render()
            path = os.path.join(folder, "{}.html".format(route_to_filename(route)))
            with open(path, 'w') as f:
                f.write(html_str)
            self.files[route] = path

    def define_routes(self):
        """ Method defining the routes in the FastAPI app, to display the right
        HTML file.
        """
        # Define the pages' routes
        for route, html_file in self.files.items():
            @self.fapi.get(route)
            def index():
                return FileResponse(html_file)

    def serve(self, folder=SWOLE_CACHE, host='127.0.0.1', port=8000, log_level='info'):
        """ Method to fire up the FastAPI server !

        Arguments:
            folder (`str`, optional): Folder where to save HTML files. Defaults
                to SWOLE_CACHE.
            host (`str`, optional): Run FastAPI on this host. Defaults to
                `127.0.0.1`.
            port (`int`, optional): Run FastAPI on this port. Defaults to
                `8000`.
            log_level (`str`, optional): Log level to use for FastAPI. Can be
                [`critical`, `error`, `warning`, `info`, `debug`, `trace`].
                Defaults to `info`.
        """
        self.write(folder=folder)
        self.define_routes()

        uvicorn.run(self.fapi, host=host, port=port, log_level=log_level)
