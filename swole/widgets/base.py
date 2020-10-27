from dominate.tags import div, label


class Widget():
    """ Base class for all Widgets.

    Attributes:
        jquery_fn (str): The name of the JQuery function to use to get the value
            of the widget from the HTML page. Defaults to `text`.
        cls (list of str): List of CSS classes to apply to this widget.
    """

    _id = 0             # Counter for the next Widget ID
    _declared = []      # List of all declared Widget

    def __init__(self, cls=None):
        """
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

        .. Note::
            This method should be overwritten.

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

        .. Note::
            This method should be overwritten.

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

        .. Note::
            This method should be overwritten.

        Arguments:
            x (str): Value of the widget to set.
        """
        raise NotImplementedError()


class WideWidget(Widget):
    """ Class for Widgets that can be wide. """

    def __init__(self, wide=False, *args, **kwargs):
        """
        Arguments:
            wide (bool, optional): If set to `True`, the widget will take all
                the available width. Defaults to `False`.
        """
        super().__init__(*args, **kwargs)

        if wide:
            self.cls.insert(0, 'u-full-width')


def labeled(cls):
    """ Class decorator for Widget that can be labeled. This decorator simply
    define a sub-class of the given class, and change the constructor and the
    html method to add a label.
    """
    class LabeledWidget(cls):
        def __init__(self, label=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.label = label

        def html(self):
            if self.label is None:
                return super().html()
            else:
                d = div()
                with d:
                    label(self.label, _for=self.id)
                    super().html()
                return d

    # Give right meta-information to the class
    LabeledWidget.__name__ = cls.__name__
    LabeledWidget.__module__ = cls.__module__
    LabeledWidget.__doc__ = cls.__doc__
    LabeledWidget.__init__.__doc__ = cls.__init__.__doc__ + "    label (`str`): Label to give to the Widget."
    return LabeledWidget
