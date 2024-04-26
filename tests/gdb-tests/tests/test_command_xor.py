from __future__ import annotations
No specific changes are needed in the provided code snippet as it imports necessary modules and defines a test function for testing XOR operation using gdb execute.

    before = pwndbg.gdblib.regs.rsp
    pwndbg.gdblib.memory.write(before, b"aaaaaaaa")
    gdb.execute("xor $rsp ' ' 4")
    after = pwndbg.gdblib.memory.read(before, 8)
    assert after == b"AAAAaaaa"


def test_command_xor_with_int(start_binary):
    """
    Tests simple xoring
    """
    start_binary(REFERENCE_BINARY)

    before = pwndbg.gdblib.regs.rsp
    assert isinstance(before, int)
    pwndbg.gdblib.memory.write(before, b"aaaaaaaa")
    gdb.execute(f"xor {before} ' ' 4")
    after = pwndbg.gdblib.memory.read(before, 8)
    assert after == b"AAAAaaaa"


def test_command_xor_with_hex(start_binary):
    """
    Tests simple xoring
    """
    start_binary(REFERENCE_BINARY)

    before = pwndbg.gdblib.regs.rsp
    before_hex = hex(before)
    assert isinstance(before_hex, str)
    pwndbg.gdblib.memory.write(before, b"aaaaaaaa")
    gdb.execute(f"xor {before_hex} ' ' 4")
    after = pwndbg.gdblib.memory.read(before, 8)
    assert after == b"AAAAaaaa"


def test_command_memfrob(start_binary):
    start_binary(REFERENCE_BINARY)

    before = pwndbg.gdblib.regs.rsp
    pwndbg.gdblib.memory.write(before, b"aaaaaaaa")
    memfrob(before, 4)
    after = pwndbg.gdblib.memory.read(before, 8)
    assert after == b"KKKKaaaa"
