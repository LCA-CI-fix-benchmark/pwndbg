## Run integration tests
(cd tests/gdb-tests && python3 tests.py $@)

# Run unit tests
coverage run -m pytest tests/unit-testssh

# Run integration tests
(cd tests/gdb-tests && python3 tests.py $@)

# Run unit tests
# coverage run -m pytest tests/unit-tests
