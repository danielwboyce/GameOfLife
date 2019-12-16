import csv


# The students.csv file contains two columns: id and name. The data from students.csv is read into a map where the key
# is the student's id and the value is the students name. This allows for easy connection between other maps, like the
# one for marks.csv, for example, where the root key is also the student's id.z
def import_students_csv_as_map(filename):
    students_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            students_map[row["id"]] = row["name"]
    return students_map


# The marks.csv file contains three columns: test_id, student_id and mark. The data from marks.csv is read into a map
# where the key is student_id and the value is another map where the key is test_id and the value is mark. This allows
# for easy connection between other maps, like the one for students.csv, for example, where the root key is also the
# student's id, or for tests.csv, where the key is test_id. This is in turn allows for easy access of the score for a
# particular student on a particular test.
def import_marks_csv_as_map_of_maps(filename):
    marks_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["student_id"] not in marks_map:
                marks_map[row["student_id"]] = {}
                marks_map[row["student_id"]][row["test_id"]] = row["mark"]
            else:
                marks_map[row["student_id"]][row["test_id"]] = row["mark"]
    return marks_map


# The tests.csv file contains three columns: id, course_id and weight. The data from tests.csv is read into a map
# where the key is id and the value is an array where the 0-index value is course_id and the 1-index value is weight.
# This allows for easy connection between other maps, like the one for marks.csv, for example, where the key for a par-
# ticular student's submap is test_id and allows you to easily tell which course a test was for and what its weight was.
def import_tests_as_map_of_arrays(filename):
    tests_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tests_map[row["id"]] = [row["course_id"], row["weight"]]
    return tests_map


# The courses.csv file contains three columns: id, name, and teacher. The data from courses.csv is read into a map where
# the key is id and the value is an array where the 0-index value is name and the 1-index value is teacher. This allows
# for easy connection between other maps, like the one for marks.csv or tests.csv where, when you have a map of tests
# taken by a particular student, you can find the mark the student received, the weight of that test in a course, the
# name of a course, and the name of the course's teacher.
def import_courses_as_map_of_arrays(filename):
    courses_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            courses_map[row["id"]] = [row["name"], row["teacher"]]
    return courses_map


# This function takes the maps generated by students.csv, marks.csv, and tests.csv, and calculates the course average
# for each course a student is taking. This data is stored in a map where the key is the student's id and the value is
# another map where the key is a course id and the value is the course score. Because the of the interrelation of all
# our previous maps, it is easy to calculate a course score by adding up the weighted scores from all the tests a
# student has taken.
def generate_course_scores(students, marks, tests):
    map_of_students_raw_grades = {}
    for student_id in students:
        map_of_students_raw_grades[student_id] = {}
    for student_id in marks:
        student_marks = marks[student_id]
        for test_id in student_marks:
            course_id = tests[test_id][0]
            mark = float(student_marks[test_id])
            weight = float(tests[test_id][1])
            weighted_score = (weight / 100) * mark
            if (course_id not in map_of_students_raw_grades[student_id]):
                map_of_students_raw_grades[student_id][course_id] = weighted_score
            else:
                map_of_students_raw_grades[student_id][course_id] += weighted_score
    return map_of_students_raw_grades


# This function performs some simple lookups on the map containing a students course scores and finds the student's
# average grade across all their courses. The data is returned as a map with the student's id as the key and their
# average as the value.
def calculate_students_averages(student_scores):
    student_averages = {}
    for student_id in student_scores:
        student_num_of_courses = len(student_scores[student_id].values())
        student_average = sum(student_scores[student_id].values()) / student_num_of_courses
        student_averages[student_id] = student_average
    return student_averages


# This function performs simple lookups across the calculated maps and the maps from students.csv and courses.csv maps
# to generate a report card string.
def make_report_card(student_scores, student_averages, students, courses):
    returned_string = ''
    for student_id in sorted(student_scores.keys()):
        student_name = students[student_id]
        student_average = student_averages[student_id]
        student_header_string = f'Student Id: {student_id}, name: {student_name}\nTotal Average:\t{student_average:2.2f}\n\n'
        returned_string += student_header_string
        for course_id in sorted(student_scores[student_id].keys()):
            course_name = courses[course_id][0]
            teacher_name = courses[course_id][1]
            course_grade = student_scores[student_id][course_id]
            course_string = f'\tCourse: {course_name}, Teacher: {teacher_name}\n\tFinal Grade:\t{course_grade:2.2f}\n\n'
            returned_string += course_string
        returned_string += '\n\n'
    return returned_string