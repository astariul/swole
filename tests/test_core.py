import pytest
from swole import Application, Page
from swole.widgets import Widget


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


def test_write_pages(scratch, tmpdir):
    Page()
    app = Application()
    app.write(folder=tmpdir)
    html_file = tmpdir.join("_.html")
    with open(html_file) as f:
        html = f.read()
    assert html == str(Page._dict['/'].html())


def test_assign_only_orphan(scratch):
    w1 = Widget()
    w2 = Widget()

    Application().assign_orphan_widgets()

    assert "/" in Page._dict
    assert Page._dict["/"].widgets[0] is w1
    assert Page._dict["/"].widgets[1] is w2


def test_assign_empty(scratch):
    Application().assign_orphan_widgets()

    assert "/" in Page._dict
    assert len(Page._dict["/"].widgets) == 0


def test_assign_orphan(scratch):
    w1 = Widget()
    w2 = Widget()
    w3 = Widget()
    p = Page("/test")
    p.add(w2)

    Application().assign_orphan_widgets()

    assert "/" in Page._dict and "/test" in Page._dict
    assert Page._dict["/"].widgets[0] is w1
    assert Page._dict["/test"].widgets[0] is w2
    assert Page._dict["/"].widgets[1] is w3


def test_assign_orphan_already_home(scratch):
    Page()
    Widget()
    Widget()

    Application().assign_orphan_widgets()

    assert "/" in Page._dict
    assert len(Page._dict["/"].widgets) == 2


@pytest.mark.parametrize("routes", [['/'], ['/', '/t1', '/t2']])
def test_define_route(scratch, routes):
    app = Application()
    app.files = {r: "whatever.html" for r in routes}
    app.define_routes()

    fapi_routes = [route.path for route in app.fapi.routes]
    for r in routes:
        assert r in fapi_routes
    assert "/callback/{callback_id}" in fapi_routes


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
