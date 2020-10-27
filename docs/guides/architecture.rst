How it works ?
==============

Swole tries to be as transparent as possible. Applications are made with `HTML`, `CSS`, and `Javascript`.

.. Note::
    You can always use the "inspect" tool of your browser on a Swole application to view the code.

Core architecture
-----------------

An application is represented by the :class:`~swole.Application` object. It contains references to one or several :class:`~swole.Page` object.

Each :class:`~swole.Page` has a unique route. The :class:`~swole.Page` is made of several :class:`~swole.widgets.Widget` object. These :class:`~swole.widgets.Widget` are the basic building blocs, used to create the content of each page.

Each type of :class:`~swole.widgets.Widget` is independently built into HTML. The HTML generated for each :class:`~swole.Page` is just the addition of HTML from each of its :class:`~swole.widgets.Widget`.

.. _styling-anchor:

Styling
-------

Styling is done using CSS, through the :class:`~swole.skins.Skin` object.

:class:`~swole.skins.Skin` is just a bunch of CSS rules. Each :class:`~swole.Page` is assigned a :class:`~swole.skins.Skin`, and the styling of the elements of the :class:`~swole.Page` is done using the rules from the :class:`~swole.skins.Skin`.

By decoupling style and content, changing the style of the page is as simple as using another :class:`~swole.skins.Skin`.

Server-client interaction
-------------------------

For server-client interaction, Swole uses **AJAX requests**.

AJAX requests allow the web application to send and receive data from the server in the background. This allow the web page to change dynamically without the need to reload the entire page.

By using AJAX requests, we also have better control of what is send and when, as developer.

AJAX requests are represented by the class :class:`~swole.Ajax`, and can be easily declared using the decorator :obj:`~swole.ajax`.
