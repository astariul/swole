from swole.widgets import Widget


def test_widget_id():
    w1 = Widget()
    w2 = Widget()
    w3 = Widget()
    assert w1.id != w2.id != w3.id
