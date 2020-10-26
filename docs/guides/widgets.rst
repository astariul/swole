Make you own Widget
===================

Swole is bundled with some general-use :class:`~swole.widgets.Widget`.
But sometimes you need more than that !

To fit your specific needs, you can create a custom :class:`~swole.widgets.Widget`.

Let's see together in this guide how to create a custom :class:`~swole.widgets.Widget`. We will create a Widget making two buttons.

Step 1 : sub-class Widget
-------------------------

Let's create a sub-class of :class:`~swole.widgets.Widget` :

.. code-block:: python

    from swole.widgets import Widget

    class TwoButtons(Widget):
        pass

Let's change the constructor to take two strings (the text of each button) :

.. code-block:: python

    class TwoButtons(Widget):
        def __init__(self, text1="Button 1", text2="Button 2", **kwargs):
            super().__init__(**kwargs)
            self.text1 = text1
            self.text2 = text2

Step 2 : create HTML
--------------------

Now we have to overwrite the method :meth:`~swole.widgets.Widget.html`, where the HTML of the :class:`~swole.widgets.Widget` is defined :

.. code-block:: python

    from dominate.tags import button, div

    class TwoButtons(Widget):
        def html(self):
            attributes = {"id": self.id}        # Best practice : Always add the ID of the Widget
            self.add_css_class(attributes)      # Method from super to add custom CSS classes
            
            d = div(**attributes)
            with d:
                button(self.text1)
                button(self.text2)
            return d

.. warning::
    You should use the `dominate <https://github.com/Knio/dominate/>`_ library to create the HTML object returned by :meth:`~swole.widgets.Widget.html`.

Step 3 : define setter and getter
---------------------------------

`setter` and `getter` are methods used by `Javascript` for the AJAX requests. It's the gateway between `Python` and `Javascript`.

In our case it's simple :

.. code-block:: python

    class TwoButtons(Widget):
        def get(self):
            return [self.text1, self.text2]

        def set(self, x):
            self.text1 = x[0]
            self.text2 = x[1]

Step 4 : define AJAX (optional)
-------------------------------

Optionally, your :class:`~swole.widgets.Widget` can also overwrite the method :meth:`~swole.widgets.Widget.ajax`. This method is used to retrieve AJAX requests linked to this :class:`~swole.widgets.Widget`. It should return a :class:`~swole.core.Ajax` object.

You can refer the implementation of :class:`~swole.widgets.Button` for an example.

Step 5 : use your widget
------------------------

You're all done ! Now you just have to use your :class:`~swole.widgets.Widget` is one of your web application !

.. code-block:: python

    TwoButtons(text2="My 2 buttons")
    
    if __name__ == "__main__":
        Application().serve()