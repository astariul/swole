import os
import enum
from typing import Dict

from fastapi import FastAPI
from starlette.responses import FileResponse
import uvicorn

from swole.core.page import Page, HOME_ROUTE
from swole.core.utils import route_to_filename
from swole.widgets import Widget


SWOLE_CACHE = "~/.cache/swole"      #: Default directory to use for caching.


class Application():
    """ Class representing an application. Application are used to serve
    declared pages.

    Attributes:
        fapi (`fastapi.FastAPI`): FastAPI app.
    """
    def __init__(self):
        self.files = None
        self.fapi = FastAPI()

    def assign_orphan_widgets(self):
        """ Method finding orphan widgets if any, and assigning it to the Home
        page. If the home page does not exist, create it. This allow a very
        simple and easy way to use the library.
        """
        if HOME_ROUTE not in Page._dict:
            # No home page : create one
            Page()

        home = Page._dict[HOME_ROUTE]
        assigned_widgets = set().union(*[page.widgets for page in Page._dict.values()])
        for w in Widget._declared:
            if w not in assigned_widgets:       # Orphan !
                home.add(w)

    def write(self, folder=SWOLE_CACHE):
        """ Method to write the HTML of the application to files, in order to
        later serve it.

        Arguments:
            folder (`str`, optional): Folder where to save HTML files. Defaults
                to :const:`~swole.core.application.SWOLE_CACHE`.
        """
        os.makedirs(folder, exist_ok=True)

        self.files = {}         # Route -> HTML file
        self.callbacks = {}     # Callback ID -> (Page, Ajax)
        for route, page in Page._dict.items():
            # Write HTML of the page
            html_str = page.html().render()
            path = os.path.join(folder, "{}.html".format(route_to_filename(route)))
            with open(path, 'w') as f:
                f.write(html_str)
            self.files[route] = path

            # Save also callbacks (along with their page)
            for aj in page.ajax():
                self.callbacks[aj.id] = (page, aj)

    def define_routes(self):
        """ Method defining the routes in the FastAPI app, to display the right
        HTML file.
        """
        # Define the pages' routes
        for route, html_file in self.files.items():
            @self.fapi.get(route)
            def index():
                return FileResponse(html_file)

        # Define the callback route
        if len(self.callbacks) != 0:
            # Define a dynamic enum to ensure only specific callback ID are valid
            cbe = enum.IntEnum('CallbackEnum', {str(c_id): c_id for c_id in self.callbacks.keys()})

            @self.fapi.post("/callback/{callback_id}")
            def callback(callback_id: cbe, inputs: Dict[str, str]):
                page, ajax = self.callbacks[callback_id]
                return ajax(page, inputs)

    def serve(self, folder=SWOLE_CACHE, host='0.0.0.0', port=8000, log_level='info'):
        """ Method to fire up the FastAPI server !

        Arguments:
            folder (`str`, optional): Folder where to save HTML files. Defaults
                to :const:`~swole.core.application.SWOLE_CACHE`.
            host (`str`, optional): Run FastAPI on this host. Defaults to
                `0.0.0.0`.
            port (`int`, optional): Run FastAPI on this port. Defaults to
                `8000`.
            log_level (`str`, optional): Log level to use for FastAPI. Can be
                [`critical`, `error`, `warning`, `info`, `debug`, `trace`].
                Defaults to `info`.
        """
        self.assign_orphan_widgets()
        self.write(folder=folder)
        self.define_routes()

        uvicorn.run(self.fapi, host=host, port=port, log_level=log_level)
