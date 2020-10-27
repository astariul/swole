FAQ
===

Why using `Swole` ? Why not `Streamlit` ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Don't get me wrong, `Streamlit` is an awesome framework. `Swole` just try to fix a few problematic issues of `Streamlit` :

- It uses `Flask`, which is outdated and not performant when compared to `FastAPI <https://fastapi.tiangolo.com/>`_
- No customization possible
- No control over user's interaction with the page
- Not transparent
- No Doge 😢

How `Swole`'s backend and frontend communicate ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike `Streamlit`, which use a system of cache and reload the page everytime someone interact with it, `Swole` uses AJAX requests to update the frontend.

Reloading the page every interaction is very inefficient, and irritating for the user's experience.

Using AJAX instead makes the whole process almost invisible for the user, and everything is more clear for the developper, because we know what data is sent when.

Why do you say `Swole` is `transparent` but `Streamlit` is `opaque` ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| On a `Swole` page, try to "view the page source" (right-click).
| Now do the same on a `Streamlit` page, and compare. 😇

Why this name ?
^^^^^^^^^^^^^^^

It all comes from a meme :

.. image:: img/meme.png