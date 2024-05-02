handle_sigint() {
    echo "Exiting..." >&2
    echo "Killing QEMU process $QEMU_PID" >&2;
    pkill -P $QEMU_PID
    exit 1
}
trap handle_sigint SIGINT

}
