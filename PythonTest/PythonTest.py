import csv

#setting value of units to 6
#MIT801 is 3 units and MIT802 is 3 units
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


def calculate_CGPA(firstScore, secondScore):
    cgpa = 0
    aGP = 0
    bGP = 0

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

    if secondScore.capitalize() == 'A':
        bGP = 15
    elif secondScore.capitalize() == 'B':
        bGP = 12
    elif secondScore.capitalize() == 'C':
        bGP = 9
    elif secondScore.capitalize() == 'D':
        bGP = 6
    elif secondScore.capitalize() == 'E':
        bGP = 3
    else:
        bGP = 0

    cgpa = (aGP + bGP) / 6
    return cgpa

#variable for holding list to be sent to CSV output file
input_list = []

#read data from input file and update input_list
with open('INPUT_TEST.csv') as csvInput:
    csv_reader = csv.reader(csvInput)
    
    for line in csv_reader:
        input_list.append(line)

    input_list[0].append('UNIT')
    input_list[0].append('CGPA')
    #skip header line after setting headers UNIT and CG

    #calculate CGPA and update required field
    for line in input_list:
        if line[1] == 'NAME':
            continue
        line.append(6)
        firstGrade = score_grade(int(line[3]))
        secondGrade = score_grade(int(line[4]))
        line.append(calculate_CGPA(firstGrade, secondGrade))

    #output file into new CSV file
    with open('OUTPUT_TEST.csv', 'w') as csvOutput:
        csv_writer = csv.writer(csvOutput, delimiter=',')
        for line in input_list:
            csv_writer.writerow(line)
        
        