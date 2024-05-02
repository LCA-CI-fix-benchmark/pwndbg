#!/bin/bash

# Run integration tests
(cd tests/gdb-tests && python3 tests.py $@)

# Run unit tests with coverage
coverage run -m pytest tests/unit-tests