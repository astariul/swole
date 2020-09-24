from swole.widgets import Widget, Input


def test_widget_id(scratch):
    w1 = Widget()
    w2 = Input()
    w3 = Widget()
    assert w1.id != w2.id != w3.id


def test_widget_declared(scratch):
    w1 = Widget()
    w2 = Input()
    w3 = Widget()
    assert Widget._declared == [w1, w2, w3]
