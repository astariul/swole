import dominate
from dominate.tags import script
from dominate.util import raw

from swole.widgets.base import Widget


JQUERY_CDN = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
COMMON_JS = """
      function callback(id, data) {
          console.log(`/callback/${id}`);
          $.ajax({
              type: "POST",
              url: `/callback/${id}`,
              data: JSON.stringify(data),
              success: function (data) {
                  for (var key in data) {
                      console.log( key, data[key] );
                  }
              },
              failure: function (errMsg) {
                  alert(errMsg);
              }
          });
      }"""


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
        js_str = "\n\n".join([a.js() for a in self.ajax()])
        if js_str != '':
            doc.add(script(src=JQUERY_CDN))
            doc.add(script(raw(js_str + "\n\n" + COMMON_JS)))

        return doc

    def add(self, widget):
        """ Method to add a widget to this page.

        Arguments:
            widget (`Widget`): Widget to add.
        """
        if not isinstance(widget, Widget):
            raise ValueError("The given argument is not a widget : {}".format(widget))

        self.widgets.append(widget)

    def ajax(self):
        """ Method to retrieve all Ajax requests of this page.

        Returns:
            list of Ajax: List of Ajax requests.
        """
        ajax = [w.ajax() for w in self.widgets]
        return [a for a in ajax if a is not None]
