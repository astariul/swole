Swole
=====

Application
-----------

.. autodata:: swole.core.application.SWOLE_CACHE

.. autoclass:: swole.Application
    :members: serve

Page
----

.. autodata:: swole.core.page.HOME_ROUTE

.. autodata:: swole.core.page.DEFAULT_FAVICON
    :annotation: = Doge

.. autoclass:: swole.Page
    :members: add
    :special-members: __enter__, __exit__

Ajax
----

.. autoclass:: swole.Ajax
    :members:
    :special-members: __call__

.. autodecorator:: swole.ajax

Skin
----

.. autoclass:: swole.skins.Skin
    :members:

utils
-----

.. autofunction:: swole.core.route_to_filename