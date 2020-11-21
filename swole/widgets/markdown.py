import dominate
from dominate.tags import div, code, pre, p
from markdown_it import MarkdownIt
from markdown_it.renderer import RendererHTML
from markdown_it.common.utils import escapeHtml

from swole.widgets.base import Widget


class DominateRenderer(RendererHTML):
    """ Custom renderer for markdown-it parser. It render Markdown using
    Dominate tags.
    """
    def _render(self, tokens, options, env):
        """ Recursive function parsing each token into the right Dominate tag.
        """
        pending_tags = []
        pending_content = [[]]
        for t, token in enumerate(tokens):
            if token.type == "fence":       # Special case
                pending_content[-1].append(self.fence(tokens, t, options, env))
            elif token.tag != "":
                if not token.nesting:       # Directly append to content
                    c = [token.content] if token.content else []
                    tag = getattr(dominate.tags, token.tag)
                    tag = tag(*c) if token.attrs is None else tag(*c, **token.attrs)
                    pending_content[-1].append(tag)
                elif len(pending_tags) > 0 and pending_tags[-1] == token.tag:       # Closing tag
                    t = pending_tags.pop()
                    c = pending_content.pop()
                    tag = getattr(dominate.tags, t)
                    tag = tag(c) if token.attrs is None else tag(c, **token.attrs)
                    pending_content[-1].append(tag)
                else:       # Opening tag
                    pending_tags.append(token.tag)
                    pending_content.append([])
            elif token.children is not None:
                assert len(token.children) > 0
                pending_content[-1].extend(self._render(token.children, options, env))
            else:
                if not token.hidden:
                    pending_content[-1].append(escapeHtml(token.content))

        assert len(pending_tags) == 0, pending_tags
        assert len(pending_content) == 1, pending_content

        return pending_content[-1]

    def render(self, tokens, options, env):
        """ Takes token stream and generates Dominate HTML.
        Check the default implementation at :
        https://github.com/executablebooks/markdown-it-py/blob/master/markdown_it/renderer.py
        """
        content = self._render(tokens, options, env)

        d = div()
        d.add(*content)
        return d

    def fence(self, tokens, idx, options, env):
        token = tokens[idx]
        # TODO : Later, add correct highlights for languages
        # info = unescapeAll(token.info).strip() if token.info else ""
        # langName = ""

        # if info:
        #     langName = info.split()[0]

        highlighted = escapeHtml(token.content)

        if token.attrs:
            return pre(code(highlighted), **token.attr)
        else:
            return pre(code(highlighted))


class Markdown(Widget):
    """ A general widget to write Markdown. """
    def __init__(self, content="", **kwargs):
        """
        Arguments:
            content (`str`, optional): Markdown content. Defaults to empty string.
        """
        super().__init__(**kwargs)
        self.content = content

    def html(self):
        md = MarkdownIt(renderer_cls=DominateRenderer).enable('table')
        html = md.render(self.content)
        html.id = self.id
        return html
        # TODO : Full markdown parsing + convertion to dominate tags
        return p(self.content, id=self.id)

    def get(self):
        return self.content

    def set(self, x):
        self.content = x
