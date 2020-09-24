import pytest
from swole.widgets import Widget


@pytest.fixture
def scratch():
    # Reinitialize the Widget class
    Widget._id = 0
    Widget._declared = []
    return None
