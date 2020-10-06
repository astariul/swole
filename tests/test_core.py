import pytest
from swole import Application, Page
from swole.widgets import Widget


@pytest.mark.parametrize("args,routes", [([], []), ([[Page(), Page('/test')]], ['/', '/test'])])
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
    app = Application([Page()])
    with pytest.raises(ValueError):
        app.add(Page())


def test_page_html():
    p = Page(skin=None, favicon=None)
    assert str(p.html()) == """<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body>
    <div class="container"></div>
  </body>
</html>"""


def test_write_pages(tmpdir):
    app = Application([Page()])
    app.write(folder=tmpdir)
    html_file = tmpdir.join("_.html")
    with open(html_file) as f:
        html = f.read()
    assert html == str(app.pages['/'].html())


def test_assign_only_orphan(scratch):
    app = Application()
    w1 = Widget()
    w2 = Widget()

    app.assign_orphan_widgets()

    assert "/" in app.pages
    assert app.pages["/"].widgets[0] is w1
    assert app.pages["/"].widgets[1] is w2


def test_assign_orphan(scratch):
    app = Application()
    w1 = Widget()
    w2 = Widget()
    w3 = Widget()
    p = Page("/test")
    p.add(w2)
    app.add(p)

    app.assign_orphan_widgets()

    assert "/" in app.pages and "/test" in app.pages
    assert app.pages["/"].widgets[0] is w1
    assert app.pages["/test"].widgets[0] is w2
    assert app.pages["/"].widgets[1] is w3


def test_assign_orphan_already_home(scratch):
    app = Application([Page()])
    Widget()
    Widget()

    app.assign_orphan_widgets()

    assert "/" in app.pages
    assert len(app.pages["/"].widgets) == 0


def test_context_manager_page(scratch):
    Widget()
    p = Page()
    with p:
        w1 = Widget()
        w2 = Widget()
    Widget()

    assert len(p.widgets) == 2
    assert w1 in p.widgets
    assert w2 in p.widgets
