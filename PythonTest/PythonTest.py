import csv

#setting value of units to 6
#MIT801 is 3 units and MIT802 is 3 units
#I have assumed all courses carry 3 units
def score_grade(score):
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


def calculate_CGPA(firstScore):
    aGP = 0

    if firstScore.capitalize() == 'A':
        aGP = 15
    elif firstScore.capitalize() == 'B':
        aGP = 12
    elif firstScore.capitalize() == 'C':
        aGP = 9
    elif firstScore.capitalize() == 'D':
        aGP = 6
    elif firstScore.capitalize() == 'E':
        aGP = 3
    else:
        aGP = 0

    return aGP

#variable for holding list to be sent to CSV output file
input_list = []

#read data from input file and update input_list
with open('INPUT_TESTUPDATE.csv', 'r') as csvInput:
    csv_reader = csv.reader(csvInput)
    columns = len(next(csv_reader)) #counts the number of columns in csv file
    csvInput.seek(0)
    
    for line in csv_reader:
        input_list.append(line)

    input_list[0].append('UNIT')
    input_list[0].append('CGPA')
    #skip header line after setting headers UNIT and CG

    #calculate CGPA and update required field
    for line in input_list:
        if line[1] == 'NAME':
            continue
        cgpa_list = []
        unit = 0

        for r in range(columns):
            if int(r) <= 2: #to skip the first 3 columns which aren't needed
                continue
            else:
                grade = score_grade(int(float(line[r].strip())))
                coursegp = calculate_CGPA(grade)
                cgpa_list.append(coursegp)
                unit += 3
        cgpa = sum(cgpa_list) / float(unit)
        line.append(unit)
        line.append(cgpa)

    #output file into new CSV file
    with open('OUTPUT_TEST.csv', 'w') as csvOutput:
        csv_writer = csv.writer(csvOutput, delimiter=',')
        for line in input_list:
            csv_writer.writerow(line)
       