<h1 align="center">dummygummy</h1>
<p align="center">Short description of the package.</p>

<p align="center"><a href="https://github.com/colanim/python-repo/actions"><img src="https://github.com/colanim/python-repo/workflows/tests/badge.svg" alt="test status" /></a></p>

<h2 align="center">Install</h2>

Simply run :

```console
pip install git+https://github.com/colanim/python-repo.git
```

<h2 align="center">Contribute</h2>

Ensure tests are passing :

```console
pip install pytest

python -m pytest -W ignore::DeprecationWarning
```

---

Check if code is well-formated :

```console
pip install flake8

flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
```

---

Generate documentation with :

```console
pip install sphinx
pip install sphinx_rtd_theme

cd docs
make html

cd docs/_build/html/
python3 -m http.server 8800
```