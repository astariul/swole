import pytest
from markdown_it import MarkdownIt
from swole.widgets.markdown import DominateRenderer, Markdown


@pytest.mark.parametrize("inp, out", [
    ("# Title 1", ""),
    ("## Title 2", ""),
    ("### Title 3", ""),
    ("#### Title 4", ""),
    ("##### Title 5", ""),
    ("###### Title 6", ""),
    ("Paragraph 1\n\nParagraph 2", ""),
    ("This *is* right", ""),
    ("This **is** right", ""),
    ("This _is_ right", ""),
    ("Paragraph 1\n\n---\n\nParapgrah 2", ""),
    ("* List 1\n* List 2", ""),
    ("This `is` code", ""),
    ("```python\nis\n```", ""),
    ])
def test_renderer(inp, out):
    md = MarkdownIt(renderer_cls=DominateRenderer).enable('table')
    assert md.render(inp) == out