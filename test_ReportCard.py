from ReportCard import import_data_as_map_of_maps

def print_students(students):
    line_count = 0
    for student_id in students:

        if line_count == 0:
            print(f'Column names are {", ".join(students[student_id])}')
            line_count += 1
        print(f'\tStudent {students[student_id]["id"]}\'s name is {students[student_id]["name"]},')


def print_courses(courses):
    line_count = 0
    for course_id in courses:
        if line_count == 0:
            print(f'Column names are {", ".join(courses[course_id])}')
            line_count += 1
        print(f'\tThe {courses[course_id]["name"]} course is taught by {courses[course_id]["teacher"]} and its ID is {courses[course_id]["id"]}.')


def print_marks(courses):
    line_count = 0
    for test_id in marks:
        if line_count == 0:
            print(f'Column names are {", ".join(marks[test_id])}')
            line_count += 1
        print(f'\tTest {marks[test_id]["test_id"]} was taken by student {marks[test_id]["student_id"]} and that student earned a {marks[test_id]["mark"]}%.')


def print_tests(tests):
    line_count = 0
    for test_id in tests:
        if line_count == 0:
            print(f'Column names are {", ".join(tests[test_id])}')
            line_count += 1
        print(f'\tTest {tests[test_id]["id"]} goes in course {tests[test_id]["course_id"]} and has a weight of {tests[test_id]["weight"]}%.')





students_filename = '/home/daniel/Downloads/backend-assessment/backend-assessment/students.csv'
courses_filename  = '/home/daniel/Downloads/backend-assessment/backend-assessment/courses.csv'
marks_filename    = '/home/daniel/Downloads/backend-assessment/backend-assessment/marks.csv'
tests_filename    = '/home/daniel/Downloads/backend-assessment/backend-assessment/tests.csv'

students =  import_data_as_map_of_maps(students_filename, "id")
courses = import_data_as_map_of_maps(courses_filename, "id")
marks = import_data_as_map_of_maps(marks_filename, "test_id")
tests = import_data_as_map_of_maps(tests_filename, "id")

print_students(students)
print_courses(courses)
print_marks(marks)
print_tests(tests)