from dominate.tags import p

from swole.widgets.base import Widget


class Markdown(Widget):
    """ A general widget to write Markdown.

    Attributes:
        content (`str`): Markdown content.
    """
    def __init__(self, content=""):
        """ Constructor.

        Arguments:
            content (`str`, optional): Markdown content. Defaults to ``.
        """
        super().__init__()
        self.content = content

    def html(self):
        # TODO : Full markdown parsing + convertion to dominate tags
        return p(self.content, id=self.id)
