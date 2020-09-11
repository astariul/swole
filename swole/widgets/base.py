class Widget():
    """ Base class for all Widgets.

    Attributes:
        id (int): The ID of the Widget. Each created Widget have his own ID.
    """

    _id = 0

    def __init__(self):
        """ Constructor. """
        Widget._id += 1
        self.id = Widget._id

    def html(self):
        """ Method to get the `dominate` HTML of the widget. This HTML needs to
        be rendered.

        Returns:
            dominate.document: HTML document corresponding to the widget.
        """
        raise NotImplementedError()

    def ajax(self):
        """ Method to get the Ajax request (if any) of the widget. Or `None` if
        there is no Ajax call for this widget.

        Returns:
            Ajax: Ajax request. `None` if there is no Ajax request.
        """
        return None
