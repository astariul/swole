Make you own Skin
=================

As mentioned in `<guides/architecture.rst#Styling>`__, you can change the skin of your webpage by simply specifying the path to the skin to use.

This means you can create your own :class:`~swole.skins.Skin` !

Structure of the Skin file
--------------------------

A :class:`~swole.skins.Skin` file is simply a `CSS` file.

But the content is devided in 3 parts :

- External CSS
- External Fonts
- Custom rules

**External CSS** and **External Fonts** are specified as commented links, one link per line. For example :

.. code-block:: css

    /* https://fonts.googleapis.com/my_font */

These links will automatically be included in the final CSS.

Finally, **Custom rules** are specified as normal CSS. For example :

.. code-block:: css

    body {
        text-align: center;
    }

**Each part is divided by an empty line.**

Use your own Skin
-----------------

Create your :class:`~swole.skins.Skin` file following the structure mentioned in previous section.

.. note::
    You can create a copy of the base skin (``swole/skins/base.css``) as starting point, it's easier !

Then, when you create your page, specify the path to your custom :class:`~swole.skins.Skin` :

.. code-block:: python

    Page(skin_path="path/to/my/custom.css")