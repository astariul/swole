import os
import tempfile

import pytest
from swole.skins import Skin


def test_base_skin():
    s = Skin()
    assert s.libs == ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css"]
    assert s.fonts == ["https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap"]


@pytest.mark.parametrize("content,libs,fonts", [("Rules", [], []),
    ("/*  */\n\nRules", [], []), ("/*  */\n\n/*  */\n\nRules", [], []),
    ("/* A */\n\n/*  */\n\nRules", ['A'], []), ("/* A */\n\n/* B */\n\nRules", ['A'], ['B']),
    ("/*  */\n\n/* B */\n\nRules", [], ['B']), ("/* A */\n\n/* B */", ['A'], ['B']),
    ("/* A */\n/* 1 */\n\n/* B */\n/* 2 */\n\nRules", ['A', '1'], ['B', '2']),
    ("/* A */\n/* 1 */\n\n/* B */\n\nRules", ['A', '1'], ['B']),
    ("/* A */\n\n/* B */\n/* 2 */\n\nRules", ['A'], ['B', '2']),
    ("/* A */\n\nRules", ['A'], [])])
def test_parse_skin_file(content, libs, fonts):
    tmp_path = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    with open(tmp_path, 'w') as f:
        f.write(content)

    s = Skin(path=tmp_path)
    assert s.libs == libs
    assert s.fonts == fonts

    os.remove(tmp_path)