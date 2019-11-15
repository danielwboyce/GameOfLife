from ReportCard import *


students_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/students.csv'
courses_filename  = '/home/daniel/Downloads/backend-assessment/backend-assessment/courses.csv'
marks_filename    = '/home/daniel/Downloads/backend-assessment/backend-assessment/marks.csv'
tests_filename    = '/home/daniel/Downloads/backend-assessment/backend-assessment/tests.csv'

students_by_id =  import_data_as_map_of_maps(students_filename, "id")
courses_by_id = import_data_as_map_of_maps(courses_filename, "id")
marks_by_student_id = import_data_as_map_of_maps(marks_filename, "test_id")
tests_by_id = import_data_as_map_of_maps(tests_filename, "id")

print(marks_by_test_id)
#print(students['1']['name'])




