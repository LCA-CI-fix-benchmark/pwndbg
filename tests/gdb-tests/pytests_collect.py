from __future__ import annotations

import os
import sys

import pytest

TESTS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests")


class CollectTestFunctionNames:
    """See https://github.com/pytest-dev/pytest/issues/2039#issuecomment-257753269"""

    def __init__(self):
        self.collected = []

    def pytest_collection_modifyitems(self, items):
No specific changes are needed in the provided code snippet as it collects and lists test function names if the collection is successful.

# easy way to exit GDB session
sys.exit(0)
