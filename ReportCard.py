import csv


def import_data_as_map_of_maps(filename, new_key_parameter):
    map_of_maps = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            map_of_maps[row[new_key_parameter]] = row
    return map_of_maps


def import_students_as_map(filename):
    students_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            students_map[row["id"]] = row["name"]
    return students_map

def import_marks_as_map_of_maps(filename):
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


def import_tests_as_map_of_arrays(filename):
    tests_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tests_map[row["id"]] = [row["course_id"], row["weight"]]
    return tests_map


def import_courses_as_map_of_arrays(filename):
    courses_map = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            courses_map[row["id"]] = [row["name"], row["teacher"]]
    return courses_map


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

            if course_id not in map_of_students_raw_grades[student_id]:
                map_of_students_raw_grades[student_id][course_id] = weighted_score
            else:
                map_of_students_raw_grades[student_id][course_id] += weighted_score
    return map_of_students_raw_grades


def calculate_students_averages(student_scores):
    student_averages = {}
    for student_id in student_scores:
        student_num_of_courses = len(student_scores[student_id].values())
        student_average = sum(student_scores[student_id].values()) / student_num_of_courses
        student_averages[student_id] = student_average
    return student_averages

def print_report_card(student_scores, student_averages, students, courses):
    for student_id in student_scores:
        student_name = students[student_id]
        student_average = student_averages[student_id]
        student_header_string = f'Student Id: {student_id}, name: {student_name}\nTotal Average:\t{student_average:2.2f}\n'
        print(student_header_string)
        for course_id in student_scores[student_id]:
            course_name = courses[course_id][0]
            teacher_name = courses[course_id][1]
            course_grade = student_scores[student_id][course_id]
            course_string = f'\tCourse: {course_name}, Teacher: {teacher_name}\n\tFinal Grade:\t{course_grade:2.2f}\n'
            print(course_string)

