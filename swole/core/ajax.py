def ajax(*args):
    """ Decorator to define Ajax objects easily.

    Arguments:
        args (list of Widget): Widget to use as input.

    Returns:
        Ajax: Ajax object with the given callable and inputs.
    """
    def define_ajax(f):
        return Ajax(callback=f, inputs=args)
    return define_ajax


class Ajax():
    """ Class representing an AJAX request. It is used as callback to update
    the webpage dynamically.

    Attributes:
        callback (callable): Function to execute when the AJAX is called.
        inputs (list of Widget): Inputs to the callback.
        trigger (Widget): Widget triggering the AJAX request.
    """

    _id = 0

    def __init__(self, callback, inputs):
        """ Constructor. Make the AJAX from the function to execute, and define
        the inputs as given.

        Arguments:
            callback (callable): Function to execute when the AJAX is called.
            inputs (list of Widget): Inputs to the callback.
            trigger (Widget): Widget triggering the AJAX request.
        """
        Ajax._id += 1
        self.id = Ajax._id
        self.callback = callback
        self.inputs = inputs

    def __call__(self, page, input_data):
        """ Main method, being called by the application with the right inputs.
        This method keep track of the value of each widget of the page, and
        based on what was changed, return only the element to change in the
        page.

        Arguments:
            page (Page): Page calling the AJAX.
            input_data (dict): Inputs data retrieved from the page after the
                AJAX request was triggered. It's a dict of `str` -> `str` where
                the key is the ID of the widget and the value is the value of
                the widget.

        Returns:
            dict: Dictionary of ID to value, containing all widgets to update.
        """
        # Update value that are given
        for inp in self.inputs:
            inp.set(input_data[str(inp.id)])

        # Keep dictionary of all current value
        prev_values = {str(w.id): w.get_str() for w in page.widgets}

        # Call the callback with the right inputs
        self.callback(*[inp.get() for inp in self.inputs])

        # After callback, see what changed
        now_values = {str(w.id): w.get_str() for w in page.widgets}

        to_update = {}
        for k in prev_values:
            if prev_values[k] != now_values[k]:
                to_update[k] = now_values[k]
        return to_update

    def js(self):
        """ Method writing Javascript equivalent for this AJAX request.

        Returns:
            `str`: Javascript equivalent.
        """
        return """
      function callback_{0}() {{
          var data = {{{1}}};
          callback({0}, data);
      }}""".format(self.id, ",".join(['{0}: $("#{0}").{1}()'.format(i.id, i.jquery_fn) for i in self.inputs]))
