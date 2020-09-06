from swole.widgets import Widget, Input


def test_widget_id():
    w1 = Widget()
    w2 = Input()
    w3 = Widget()
    assert w1.id != w2.id != w3.id
