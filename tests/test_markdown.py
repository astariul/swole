import pytest
from markdown_it import MarkdownIt
from swole.widgets.markdown import DominateRenderer


@pytest.mark.parametrize("inp, out", [
    ("# Title 1", "<div><h1>Title 1</h1></div>"),
    ("## Title 2", "<div><h2>Title 2</h2></div>"),
    ("### Title 3", "<div><h3>Title 3</h3></div>"),
    ("#### Title 4", "<div><h4>Title 4</h4></div>"),
    ("##### Title 5", "<div><h5>Title 5</h5></div>"),
    ("###### Title 6", "<div><h6>Title 6</h6></div>"),
    ("Paragraph 1\n\nParagraph 2", "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"),
    ("This *is* right", "<div><p>This <em>is</em> right</p></div>"),
    ("This **is** right", "<div><p>This <strong>is</strong> right</p></div>"),
    ("This _is_ right", "<div><p>This <em>is</em> right</p></div>"),
    ("Paragraph 1\n\n---\n\nParapgrah 2", "<div><p>Paragraph 1</p><hr><p>Parapgrah 2</p></div>"),
    ("* List 1\n* List 2", "<div><ul><li>List 1</li><li>List 2</li></ul></div>"),
    ("This `is` code", "<div><p>This <code>is</code> code</p></div>"),
    ("```python\nis\n```", "<div><pre><code>is\n</code></pre></div>"),
    ("Line 1\nLine 2", "<div><p>Line 1<br>Line 2</p></div>"),
    ])
def test_renderer(inp, out):
    md = MarkdownIt(renderer_cls=DominateRenderer).enable('table')
    dominate = md.render(inp)
    print()
    assert dominate.render(pretty=False) == out
