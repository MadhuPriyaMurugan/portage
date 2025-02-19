# Copyright 2015-2021 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

doc = """Nested plug-in module for repoman LineChecks.
Performs nested subshell checks on ebuilds."""
__doc__ = doc[:]


module_spec = {
    "name": "do",
    "description": doc,
    "provides": {
        "nesteddie-check": {
            "name": "nesteddie",
            "sourcefile": "nested",
            "class": "EbuildNestedDie",
            "description": doc,
        },
    },
    "version": 1,
}
