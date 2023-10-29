#!/bin/bash

# Number of tests passed
PASSED=0

# Number of tests failed
FAILED=0

# For every input file in samples
for INPUT_FILE in samples/*.in; do
    # Derive the corresponding output file
    OUTPUT_FILE="${INPUT_FILE%.in}.out"

    # Run the solution.py with the input and capture the output
    OUTPUT=$(python3 solution.py < $INPUT_FILE)

    # Read the expected output from the output file
    EXPECTED_OUTPUT=$(cat $OUTPUT_FILE)

    # Check if the output matches the expected output
    if [ "$OUTPUT" == "$EXPECTED_OUTPUT" ]; then
        echo "Test $(basename $INPUT_FILE) PASSED"
        PASSED=$((PASSED+1))
    else
        echo "Test $(basename $INPUT_FILE) FAILED"
        echo "Expected:"
        echo "$EXPECTED_OUTPUT"
        echo "Got:"
        echo "$OUTPUT"
        FAILED=$((FAILED+1))
    fi
done

echo ""
echo "$PASSED tests passed."
echo "$FAILED tests failed."

# If any test failed, exit with a non-zero exit code
if [ $FAILED -ne 0 ]; then
    exit 1
fi

