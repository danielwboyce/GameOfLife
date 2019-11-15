import csv


def import_data_as_map_of_maps(filename, new_key_parameter):
    map_of_maps = {}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            map_of_maps[row[new_key_parameter]] = row
    return map_of_maps


def generate_report_cards(students, courses, marks, tests):
    map_of_students_raw_grades = {}
    for student_id in students:
        map_of_students_raw_grades[student_id] = {}
    for test_id in tests:
        map_of_students_raw_grades[tests[test_id]["course_id"]] = tests[test_id]