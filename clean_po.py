#!/usr/bin/env python
# Clean up the generated .po file
# Copyright Gerard Krol
# License: MIT

import sys
import re

contents = sys.stdin.read()
contents = contents.replace("""msgid ""\n"\\n"\n""","""msgid ""\n""")
# remove whitespace at start of line
contents = re.sub(r"\"[ \t]+", "\"", contents)
# remove empty strings at end
contents = re.sub(r"""^""\nmsgstr""","""msgstr""", contents, flags=re.MULTILINE)
# strip trailing newlines
contents = contents.replace("""\\n"\nmsgstr""",""""\nmsgstr""")

sys.stdout.write(contents)
