# A GDScript linter using GDQuest's GDScript-formatter.
#
# Copyright © 2026, Chris Herborth (chrish@pobox.com)
#
# Released under the Creative Commons CC-BY-NC 4.0 license. See LICENSE for
# details.

# Needed for Python 3.7+, not necessary in 3.14+
from __future__ import annotations

from SublimeLinter.lint import Linter


class GDScriptFormatterLinter(Linter):
    cmd: tuple[str] = (
        "gdscript-formatter",
        "lint"
    )
    regex: str = r'^(?P<filename>.+?):(?P<line>\d+):(?P<code>[a-z\-]+):(?P<error_type>[a-z]+): (?P<message>.*)$'
    multiline: bool = False
    defaults: dict[str, str] = {  # noqa: RUF012
        'selector': 'source.gdscript'
    }
