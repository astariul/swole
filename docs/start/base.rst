Create your own app
===================

Let's create your first app with `Swole`, step by step.

Step 1 : Add some Input Widgets
-------------------------------

In a python file (let's name it ``app.py``), import and create Widgets :

.. code-block:: python

    from swole.widgets import Input, Markdown

    i_a = Input()
    i_b = Input()
    m = Markdown("Result : ")

Step 2 : Add an AJAX request
----------------------------

To make our app interactive, we create an AJAX request that will be called when we click on a button. This AJAX request will simply compute the result of an addition :

.. code-block:: python

    from swole.widgets import button
    from swole import ajax

    @ajax(i_a, i_b)
    def addition(a, b):
        res = a + b
        m.set("Result : {}".format(res))

    Button("Compute", onclick=addition)

Step 3 : Serve your app
-----------------------

Finally add the code to serve the app in the ``main`` :

.. code-block:: python

    from swole import Application

    if __name__ == "__main__":
        Application().serve()

Step 4 : Start your app
-----------------------

Now that the code is written, you can start your app with :

.. code-block::

    python app.py

You can visit `127.0.0.1:8000 <http://127.0.0.1:8000>`_ and see your app running !
