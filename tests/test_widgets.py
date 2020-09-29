import pytest
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


@pytest.mark.parametrize("kwargs,cls", [({}, []), ({'cls': None}, []),
                                        ({'cls': []}, []), ({'cls': "None"}, ["None"]),
                                        ({'cls': ['1', '2', '3']}, ['1', '2', '3']),
                                        ({'cls': ['1', '2', '2']}, ['1', '2']),
                                        ({'cls': [1, 2, 3]}, [])])
def test_widget_cls(kwargs, cls):
    w1 = Widget(**kwargs)
    assert set(w1.cls) == set(cls)


def test_widget_cls_error():
    with pytest.raises(ValueError):
        Widget(cls=1)
