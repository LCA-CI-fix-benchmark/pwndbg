from __future__ import annotations
import os
import sys

import pytest

use_pdb = os.environ.get("USE_PDB") == "1"

sys._pwndbg_unittest_run = True

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

try:
    test_file = os.path.join(CURRENT_DIR, os.environ["PWNDBG_LAUNCH_TEST"])
except KeyError:
    print("Error: PWNDBG_LAUNCH_TEST environment variable not set.")
    sys.exit(1)

args = [test_file, "-vvv", "-s", "--showlocals", "--color=yes"]

if use_pdb:
    args.append("--pdb")

print(f"Launching pytest with args: {args}")

return_code = pytest.main(args)

if return_code != 0:
    print("-" * 80)
    print("If you want to debug tests locally, run ./tests.sh with the --pdb flag")
    print("-" * 80)

sys.exit(return_code)
