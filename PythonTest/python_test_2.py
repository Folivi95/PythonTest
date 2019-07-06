import csv
import time


def get_score_grade(score):
    grade = ''
    if score >= 70:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    elif score >= 45:
        grade = 'D'
    elif score >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return grade


def get_grade_point(grade):
    grade_point = 0

    if grade.capitalize() == 'A':
        grade_point = 15
    elif grade.capitalize() == 'B':
        grade_point = 12
    elif grade.capitalize() == 'C':
        grade_point = 9
    elif grade.capitalize() == 'D':
        grade_point = 6
    elif grade.capitalize() == 'E':
        grade_point = 3
    else:
        grade_point = 0

    return grade_point


# variable for holding list to be sent to CSV output file
input_list = []


def read_from_file(path):
    columns = 0
    try:
        with open(path, 'r') as csv_input_file:
            csv_file_reader = csv.reader(csv_input_file)
            columns = len(next(csv_file_reader))  # counts the number of columns in csv file
            csv_input_file.seek(0)
            print('no of colums in func: ' + str(columns))
            for line in csv_input_file:
                input_list.append(line)

            input_list[0].append('UNIT')
            input_list[0].append('CGPA')

    except:
        print('Something went wrong reading the file!')
    return columns


def calculate_cgpa(path):
    try:
        with open(path, 'r') as csv_input_file:
            csv_reader = csv.reader(csv_input_file)
            columns = len(next(csv_reader))  # counts the number of columns in csv file
            csv_input_file.seek(0)
            print('please wait ... reading file... ' + path)
            time.sleep(2)
            for line in csv_reader:
                input_list.append(line)

            input_list[0].append('UNIT')
            input_list[0].append('CGPA')
            # skip header line after setting headers UNIT and CG

            # calculate CGPA and update required field
            for line in input_list:
                if line[1] == 'NAME':
                    continue
                cgpa_list = []
                unit = 0

                for r in range(columns):
                    if int(r) <= 2:  # to skip the first 3 columns which aren't needed
                        continue
                    else:
                        grade = get_score_grade(int(float(line[r].strip())))
                        coursegp = get_grade_point(grade)
                        cgpa_list.append(coursegp)
                        unit += 3
                cgpa = sum(cgpa_list) / float(unit)
                line.append(unit)
                line.append(cgpa)
        print('please wait ... calculating student CGPA... ')
        time.sleep(2)
    except:
        print('something went wrong!')

    return input_list


def write_to_file(path, content):
    try:
        with open(path, 'w') as csv_output_file:
            csv_file_writer = csv.writer(csv_output_file, delimiter=',')
            print('please wait ... writing into file... ' + path)
            time.sleep(2)
            for line in content:
                csv_file_writer.writerow(line)

            print('File written successfully!')
    except IOError:
        print('Something went wrong writing the file!')


calculated_cgpa_list = calculate_cgpa('INPUT_TESTUPDATE.csv')

write_to_file('OUTPUT_TEST.csv', calculated_cgpa_list)

