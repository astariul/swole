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

    def __call__(self, page, *inputs):
        """ Main method, being called by the application with the right inputs.
        This method keep track of the value of each widget of the page, and
        based on what was changed, return only the element to change in the
        page.

        Arguments:
            page (Page): Page calling the AJAX.
            inputs (list of positional arguments): Inputs retrieved from the
                page after the AJAX request was triggered.

        Returns:
            dict: Dictionary of ID to value, containing all widgets to update.
        """
        prev_values = {w.id: w.value for w in page.widgets}

        self.callback(*inputs)

        now_values = {w.id: w.value for w in page.widgets}

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
        $.ajax({{
            type: "GET",
            url: "/callback/{0}",
            data: JSON.stringify(data),
            success: function (data) {{
                for (var key in data){{
                    console.log( key, data[key] );
                }}
            }},
            failure: function (errMsg) {{
                alert(errMsg);
            }}
        }});
    }}
""".format(self.id, ",".join(['{0}: $("#{0}").text()'.format(i.id) for i in self.inputs]))
