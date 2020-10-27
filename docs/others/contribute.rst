Contribute
==========

.. note::
    The library is in alpha version, any help is greatly appreciated, as well as ideas !

To contribute, simply fork the repository, clone it locally, install the library and create your own branch :

.. code-block:: console

    git clone https://github.com/astariul/swole.git
    cd swole
    pip install -e .
    git checkout -b my_branch

----

Add your `dogesome` code !

.. note::
    Don't forget to update tests and documentation as well !

----

Check if your code is well-formated :

.. code-block:: console

    pip install flake8

    flake8 . --count --max-complexity=10 --max-line-length=127 --statistics --per-file-ignores="__init__.py:F401"

----

Ensure tests are passing :

.. code-block:: console

    pip install pytest

    python -m pytest -W ignore::DeprecationWarning

----

Then push your changes in your fork and submit your PR !