import pytest
from swole import Application, Page


@pytest.mark.parametrize("args,routes", [([], ['/']), ([[Page(), Page('/test')]], ['/', '/test'])])
def test_application_constructor(args, routes):
    app = Application(*args)
    for route in routes:
        assert route in app.pages
        assert app.pages[route].route == route


def test_application_add_page():
    app = Application()
    app.add(Page('/test'))
    assert '/test' in app.pages


def test_application_add_several_pages():
    app = Application()
    app.add([Page('/test1'), Page('/test2')])
    assert '/test1' in app.pages and '/test2' in app.pages


def test_application_add_wrong_object():
    app = Application()
    with pytest.raises(ValueError):
        app.add(2)


def test_application_add_existing_route():
    app = Application()
    with pytest.raises(ValueError):
        app.add(Page())


def test_page_html():
    p = Page()
    assert str(p.to_html()) == """<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body></body>
</html>"""
