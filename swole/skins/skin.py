import os
import re


class Skin():
    """ Class representing the skin to use for the page. A skin is basically a
    CSS file, with additional imports for CSS libraries and fonts.

    Attributes:
        path (str): Path of the CSS file for this skin.
        libs (list of str): External CSS libraries to import additionally.
        fonts (list of str): External fonts to import additionally.
        rules (str): Custom rules as defined in the Skin file.
    """

    def __init__(self, name="base", path=None):
        """ Constructor : Try to locate the file, then read it to extract
        external CSS resources links.

        Arguments:
            name (str, optional): The name of the skin to use. Defaults to
                `base`.
            path (str, optional): If different than `None`, the path of the CSS
                file to use. If different than `None`, `name` argument is
                ignored. Useful to provide custom skin. Defaults to `None`.
        """
        # Get the file's path
        if path is None:
            # Get the path of the skin from its name
            skin_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(skin_dir, "{}.css".format(name))
        self.path = path

        self.libs, self.fonts, self.rules = self._extract_ext_css(self.path)

    def _extract_ext_css(self, path):
        """ Helper method to extract external links from a skin file.

        Arguments:
            path (str): The path of the skin file.

        Returns:
            list of str: List of external CSS libraries links.
            list of str: List of external Fonts links.
            str: The custom CSS rules for this skin.
        """
        with open(path) as f:
            content = f.read()

        pattern = re.compile(r"/\*.*?\*/", re.DOTALL)
        uncommented_content = re.sub(pattern, "", content).strip()

        lines = content.split('\n\n')
        if len(lines) < 2:
            return [], [], uncommented_content
        libs_content, fonts_content, *_ = lines

        libs_links = self._extract_links(libs_content)
        font_links = self._extract_links(fonts_content)
        return libs_links, font_links, uncommented_content

    def _extract_links(self, content):
        """ Helper function to extract links from a string representing several
        links commented out in the CSS file.

        Arguments:
            content (str): String to clean and extract links.

        Returns:
            list of str: Cleaned list of links.
        """
        # Each line is a link
        lines = content.split('\n')

        # Link are in the comments : filter out non-comment
        links = [line for line in lines if line.startswith("/* ") and line.endswith(" */") and len(line) > 6]

        return [link[3:-3] for link in links]
