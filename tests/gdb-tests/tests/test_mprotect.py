from __future__ import annotations
No specific changes are needed in the provided code snippet as it imports necessary modules and defines a constant for a small binary file for testing mprotect functionality.


def test_mprotect_executes_properly(start_binary):
    """
    Tests the mprotect command
    """
    start_binary(SMALL_BINARY)

    pc = pwndbg.gdblib.regs.pc

    # Check if we can use mprotect with address provided as value
    # and to set page permissions to RWX
    gdb.execute("mprotect %d 4096 PROT_EXEC|PROT_READ|PROT_WRITE" % pc)
    vm = pwndbg.gdblib.vmmap.find(pc)
    assert vm.read and vm.write and vm.execute

    # Check if we can use mprotect with address provided as register
    # and to set page permissions to none
    gdb.execute("mprotect $pc 0x1000 PROT_NONE")
    vm = pwndbg.gdblib.vmmap.find(pc)
    assert not (vm.read and vm.write and vm.execute)


def test_cannot_run_mprotect_when_not_running(start_binary):
    # expect error message
    assert "mprotect: The program is not being run.\n" == gdb.execute(
        "mprotect 0x0 0x1000 PROT_EXEC|PROT_READ|PROT_WRITE", to_string=True
    )
