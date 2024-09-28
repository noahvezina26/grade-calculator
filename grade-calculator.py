#This program calculates the weighted grade of a student

labs = int(input("Enter the number of labs completed: "))
if labs > 6:
    labs = 6
lab_grade = (labs/6 * 20)

quizzes = int(input("Enter the number of quizzes completed: "))
if quizzes > 6:
    quizzes = 6
quizz_grade = (quizzes/6 * 15)

assignments = []
assignments.append(int(input("Enter grade for Assignment 1: ")))
assignments.append(int(input("Enter grade for Assignment 2: ")))
assignments.append(int(input("Enter grade for Assignment 3: ")))
assignments.append(int(input("Enter grade for Assignment 4: ")))
assignment_grade = (sum(assignments)/4 * 0.16)

midterms = []
midterms.append(int(input("Enter grade for Midterm 1: ")))
midterms.append(int(input("Enter grade for Midterm 2: ")))
midterm_grade = (sum(midterms)/2 * 0.25)

final = int(input("Enter grade for Final Exam: "))
final_grade = (final * 0.18)

prep = int(input("Enter grade for Midterms and Final Preparation: "))
prep_grade = (prep * 0.06)

grade = round(lab_grade + quizz_grade + assignment_grade + midterm_grade + final_grade + prep_grade, 2)

print(f"Your grade is: {grade}")

