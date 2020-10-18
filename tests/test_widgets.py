import pytest
from swole.widgets import Widget, Input, Header


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


@pytest.mark.parametrize("level,err", [(0, True), (1, False), (2, False), (3, False),
                                       (4, False), (5, False), (6, False), (7, True),
                                       (100, True), ("1", True), ("whatever", True),
                                       (1.2, True), ([1], True)])
def test_header_error(level, err):
    try:
        Header(level=level)
    except ValueError:
        assert err
    else:
        assert not err
