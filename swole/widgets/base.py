class Widget():
    """ Base class for all Widgets.

    Attributes:
        id (int): The ID of the Widget. Each created Widget have his own ID.
        jquery_fn (str): The name of the JQuery function to use to get the value
            of the widget from the HTML page.
        cls (list of str): List of CSS classes to apply to this widget.
    """

    _id = 0             # Counter for the next Widget ID
    _declared = []      # List of all declared Widget

    def __init__(self, cls=None):
        """ Constructor. 
        
        Arguments:
            cls (str or list of str, optional): Class(es) to add to the Widget.
                Can be a single class (`str`) or several classes (`list of
                str`). If `None` is given, no additional class is added.
                Defaults to `None`.
        """
        Widget._id += 1
        Widget._declared.append(self)
        self.id = Widget._id
        self.jquery_fn = "text"

        if cls is None:
            self.cls = []
        elif isinstance(cls, str):
            self.cls = [cls]
        elif isinstance(cls, list):
            self.cls = [c for c in set(cls) if isinstance(c, str)]
        else:
            raise ValueError("The given CLS class should be a string or a list of string")

    def add_css_class(self, attr):
        """ Utils method to add the class attribute in the given dictionary.
        This dictionary can then be used in `dominate`.

        Arguments:
            attr (dict): The attributes dictionary to be used in `dominate` tag
                class.
        """
        if len(self.cls) != 0:
            attr["cls"] = " ".join(self.cls)

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


class WideWidget(Widget):
    """ Class for Widgets that can be wide.

    Attributes:
        wide (bool): If set to `True`, the widget will take all the available
            width.
    """

    def __init__(self, wide=False, *args, **kwargs):
        """ Constructor.
        
        Arguments:
            wide (bool, optional): If set to `True`, the widget will take all
                the available width. Defaults to `False`.
        """
        super().__init__(*args, **kwargs)

        if wide:
            self.cls.insert(0, 'u-full-width')
