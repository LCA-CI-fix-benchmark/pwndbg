from __future__ import annotations

import os
import shutil
import tempfile

import gdb
import pytest

import pwndbg.gdblib.info
import pwndbg.glibc
import tests

# We used the same binary as heap tests since it will use libc, and many functions are mainly for debugging the heap
HEAP_MALLOC_CHUNK = tests.binaries.get("heap_malloc_chunk.out")


@pytest.mark.parametrize(
    "have_debugging_information", [True, False], ids=["does-not-have-(*)", "have-(*)"]
)
def test_parsing_info_sharedlibrary_to_find_libc_filename(start_binary, have_debugging_information):
    # Check if we can find the libc if nothing special happens
    if not have_debugging_information:
        # Make sure the (*) in the output of `info sharedlibrary` won't affect the result
No syntax errors were found in the provided code snippet.

    # Create 3 copies of the libc with the filenames: libc-2.36.so, libc6_2.36-0ubuntu4_amd64.so, libc.so
No syntax errors were found in the provided code snippet.
            start_binary(HEAP_MALLOC_CHUNK)
            gdb.execute("break break_here")
            gdb.execute("continue")
            # Check if we can find the libc loaded by LD_PRELOAD
            if not have_debugging_information:
                assert "(*)" in pwndbg.gdblib.info.sharedlibrary()
            assert pwndbg.glibc.get_libc_filename_from_info_sharedlibrary() == test_libc_path

        # Unfortunatly, if we used LD_PRELOAD to load libc, we might cannot find the libc's filename
        # In this case, the function should return None instead of crashing
        test_libc_path = os.path.join(tmp_dir, "a_weird_name_that_does_not_look_like_a_1ibc.so")
        shutil.copy(libc_path, test_libc_path)
        gdb.execute(f"set environment LD_PRELOAD={test_libc_path}")
        start_binary(HEAP_MALLOC_CHUNK)
        gdb.execute("break break_here")
        gdb.execute("continue")
        assert pwndbg.glibc.get_libc_filename_from_info_sharedlibrary() is None
