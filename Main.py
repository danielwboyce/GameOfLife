from ReportCard import *

# The files where the data are stored
students_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/students.csv'
courses_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/courses.csv'
marks_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/marks.csv'
tests_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/tests.csv'

# Conversion from .csv files into maps of various structures. Further explanation of their structure is given in ReportCard.py and README.md
students_map = import_students_as_map(students_filename)
courses_map = import_courses_as_map_of_arrays(courses_filename)
marks_map = import_marks_as_map_of_maps(marks_filename)
tests_map = import_tests_as_map_of_arrays(tests_filename)

# This function calculates the score the student got in each course and stores it in a map of maps.
student_scores = generate_course_scores(students_map, marks_map, tests_map)

# This function calculates each student's average score across all their courses
student_averages = calculate_students_averages(student_scores)

print_report_card(student_scores, student_averages, students_map, courses_map)




