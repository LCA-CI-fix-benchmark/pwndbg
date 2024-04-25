#!/bin/bash
# Run integration tests
(cd tests/gdb-tests && python3 tests.py $@)

# Run unit tests
pytest tests/unit-tests