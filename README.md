<h1 align="center">swole</h1>
<p align="center">
Streamlit, but better.
</p>

_⚠️ For now this is an Alpha version, only a **proof-of-concept**. Only minimal features are implemented_

<p align="center">
    <a href="https://github.com/astariul/swole/actions"><img src="https://github.com/astariul/swole/workflows/tests/badge.svg" alt="test status" /></a>
    <a href="https://github.com/astariul/swole/releases"><img src="https://img.shields.io/github/v/release/astariul/swole" alt="release" /></a>
    <a href="https://swole.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/swole/badge/?version=latest" alt="doc status" /></a>
</p>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="https://github.com/astariul/swole/tree/master/examples">Examples</a> •
  <a href="#faq">FAQ</a> •
  <a href="#contribute">Contribute</a>
  <br>
  <a href="https://swole.readthedocs.io/en/stable/" target="_blank">Documentation</a>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/astariul/swole/master/.github/swole.png" width="350">
</p>

<h2 align="center">Description</h2>

[`streamlit`](https://github.com/streamlit/streamlit) is a framework that let you build beautiful apps in only a few lines of code, with only pure python.

`swole` is doing the same job, with additional features :

* **⚡ Highly performant** with [`FastAPI`](https://fastapi.tiangolo.com/) as backend
* **🦋 Easily customizable** through the usage of skins
* **💎 Transparent** (`streamlit` is opaque)
* **<img src="https://raw.githubusercontent.com/astariul/swole/master/.github/emoji.png" width="24"> Doge power !**


<h2 align="center">Install</h2>

Simply run :

```console
pip install swole
```

<h2 align="center">Usage</h2>

Create a few `Widget` for your page :

```python
from swole.widgets import Input, Button, Markdown

i_a = Input()
i_b = Input()
m = Markdown("Result : ")
```

---

Add some callbacks through AJAX requests :

```python
from swole import ajax

@ajax(i_a, i_b)
def addition(a, b):
    res = a + b
    m.set("Result : {}".format(res))

Button("Compute", onclick=addition)
```

---

Serve your app :

```python
from swole import Application

if __name__ == "__main__":
    Application().serve()
```

---

Visit [`127.0.0.1:8000`](http://127.0.0.1:8000) :

<p align="center">
    <img src="https://user-images.githubusercontent.com/40822797/105612487-d9f9c300-5dff-11eb-8919-efbd3ff07df4.gif" width="79%">
</p>

---

_For more examples, check the [`examples`](https://github.com/astariul/swole/tree/master/examples) folder !_

<h2 align="center">FAQ</h2>

#### **Why using `swole` ? Why not `streamlit` ?**

Don't get me wrong, `streamlit` is an awesome framework. `swole` just try to fix a few problematic issues of `streamlit` :

* It uses `Flask`, which is outdated and not performant when compared to `FastAPI`.
* No customization possible
* No control over user's interaction with the page
* Not transparent
* No Doge 😢

#### **How `swole`'s backend and frontend communicate ?**

Unlike `streamlit`, which use a system of cache and reload the page everytime someone interact with it, `swole` uses AJAX requests to update the frontend.

Reloading the page every interaction is very inefficient, and irritating for the user's experience.

Using AJAX instead makes the whole process almost invisible for the user, and everything is more clear for the developer because we know what data is sent when.

#### **Why do you say `swole` is "transparent" but `streamlit` is "opaque" ?**

On a `swole` page, try to "view the page source" (right-click).  
Now, do the same on a `streamlit` page, and compare. 😇 

#### **Why this name ?**

It all comes from a meme :

<p align="center">
    <img src="https://raw.githubusercontent.com/astariul/swole/master/.github/meme.png" width="450">
</p>

<h2 align="center">Contribute</h2>

Fork the repository, clone it locally, install it and create your own branch :

```console
git clone https://github.com/astariul/swole.git
cd swole
pip install -e .
git checkout -b my_branch
```

---

Add your dogesome code !

_Don't forget to update tests and documentation !_

---

Check if code is well-formated :

```console
pip install flake8

flake8 . --count --max-complexity=10 --max-line-length=127 --statistics --per-file-ignores="__init__.py:F401"
```

---

Ensure tests are passing :

```console
pip install pytest

python -m pytest -W ignore::DeprecationWarning
```

---

Submit your PR !