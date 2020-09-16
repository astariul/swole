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
        self.jquery_fn = "text"

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

    def get(self):
        """ Method to get the current value of the widget.

        Returns:
            object: Current value of the widget.
        """
        raise NotImplementedError()

    def get_str(self):
        """ Method to get the current value of the widget, as a string.

        Returns:
            str: Current value of the widget.
        """
        return str(self.get())

    def set(self, x):
        """ Method to set the current value of the widget.

        Arguments:
            x (str): Value of the widget to set.
        """
        raise NotImplementedError()
