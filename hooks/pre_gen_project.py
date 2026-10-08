"""Stop cookiecutter and cruft: this fork is used through copier only."""

import sys

sys.exit(
    "This fork of scientific-python/cookie supports copier only; "
    "cookiecutter and cruft are disabled. See FORK.md."
)
