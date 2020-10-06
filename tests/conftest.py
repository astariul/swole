import pytest
from swole import Page
from swole.widgets import Widget


@pytest.fixture
def scratch():
    # Reinitialize the Widget class
    Widget._id = 0
    Widget._declared = []
    # Reinitialize the Page class
    Page._dict = {}
    return None
