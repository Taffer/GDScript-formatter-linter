# A GDScript linter using GDQuest's GDScript-formatter's lint mode.
#
# Copyright © 2026, Chris Herborth (chrish@pobox.com)
#
# Released under the Creative Commons CC-BY-NC 4.0 license. See LICENSE for
# details.

# Needed for Python 3.7+, not necessary in 3.14+
from __future__ import annotations

from SublimeLinter.lint import Linter


class GDScriptFormatter(Linter):
    cmd: tuple[str] = ("gdscript-formatter", "lint", "${args}", "${temp_file}")
    defaults: dict[str, str] = {  # noqa: RUF012
        "selector": "source.gdscript"
    }
    multiline: bool = False
    name: str = "gdscript-formatter"
    regex: str = (
        r"^(?P<filename>.+?):"
        + r"(?P<line>\d+):"
        + r"(?P<code>[a-z\-]+):"
        + r"(?P<error_type>[a-z]+): "
        + r"(?P<message>.+?(?P<near>'[^']+'){1}?.*)$"
    )
    tempfile_suffix = ".gd"
