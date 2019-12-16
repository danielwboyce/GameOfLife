#!/bin/bash
# Run tests

# Test of the data provided by Hatchways
python3 Main.py ./test_data/provided_test/courses.csv ./test_data/provided_test/marks.csv ./test_data/provided_test/students.csv ./test_data/provided_test/tests.csv ./test_data/provided_test/output.txt

# Test of the first set of data I generated
python3 Main.py ./test_data/my_test_1/courses.csv ./test_data/my_test_1/marks.csv ./test_data/my_test_1/students.csv ./test_data/my_test_1/tests.csv ./test_data/my_test_1/output.txt
