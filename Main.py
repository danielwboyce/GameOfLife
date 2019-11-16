from ReportCard import *
import sys


# The files where the data are stored
courses_filename = sys.argv[1]
marks_filename = sys.argv[2]
students_filename = sys.argv[3]
tests_filename = sys.argv[4]

# Conversion from .csv files into maps of various structures. Further explanation of their structure is given in ReportCard.py.
students_map = import_students_csv_as_map(students_filename)
courses_map = import_courses_as_map_of_arrays(courses_filename)
marks_map = import_marks_csv_as_map_of_maps(marks_filename)
tests_map = import_tests_as_map_of_arrays(tests_filename)

#print(f'Students: {students_map}')
#print(f'Courses: {courses_map}')
#print(f'Marks: {marks_map}')
#print(f'Tests: {tests_map}')

# This function calculates the score the student got in each course and stores it in a map of maps.
student_scores = generate_course_scores(students_map, marks_map, tests_map)

# This function calculates each student's average score across all their courses
student_averages = calculate_students_averages(student_scores)

report_card = make_report_card(student_scores, student_averages, students_map, courses_map)
#print(report_card)
output_file = open(sys.argv[5],'w+')
output_file.write(report_card)
output_file.close()



