# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:34:37 2023

@author: Araba Ocran, UA ID:  001495953, INF308

"""

"""
Gradebook assignment

Goal: calculate the letter grade for each of the students in a professor’s class. 
How: prompt the user to enter their number of students they have in their class and a grade for each student in the class
Outcomes: 
        display a letter grade for each student’s grade
        display the average numeric and letter grade for the class


Function1 :convert_to_letter_grade(numericScore) is a function that will take in the student’s numeric score

Function2: compute_class_average(numStudents, sumOfClassGrades) =>>  take number of students in the class and sum of all grades and return the class average
Function3: convert_to_letter_grade(numericScore) =>> get average letter grade for the class
Function 4: main() function:  will  prompts to enter the number of students in the course and then a loop that will prompt the user to enter each students grade, calculate a running total of the students’ scores, call the appropriate functions listed above, 

"""
#testing an intro
print("Hello, welcome to your gradebook professor!!")

profName = input("Please enter your Name:")
courseName = input("please enter name of your class or course: ")
print("Hi " + profName + ",")

# create function 4: main() function:  will  prompts to enter the number of students in the course and then a loop that will prompt the user to enter each students grade, calculate a running total of the students’ scores, call the appropriate functions listed above, 

# create input promt for user to enter # of students
#num_students = int(input("please enter the number of students in your course- " + courseName +": "))
sum_of_grades = 0

# define grade book scale aka "convert_to_letter_grade(numericScore)"
def convert_to_letter_grade(numericScore):
    if numericScore >= 94:
        return 'A'
    elif numericScore >= 89:
        return 'A-'
    elif numericScore >= 85:
        return 'B+'
    elif numericScore >= 82:
        return 'B'
    elif numericScore >= 79:
        return 'B-'
    elif numericScore >= 76:
        return 'C+'
    elif numericScore >= 73:
        return 'C'
    elif numericScore >= 70:
        return 'C-'
    elif numericScore >= 67:
        return 'D+'
    elif numericScore >= 64:
        return 'D'
    elif numericScore >= 60:
        return 'D-'
    else:
        return 'E'
    
    
     
# create function2 (class-compute-avg) - that will take # of students in the class and sum of all grades and return the class average  
#  'def' keyword is used to create, (or define) a function.
# and
# 'return' keyword is used to exit a function and return a value.



def compute_class_average(numStudents, sumOfClassGrades):
    classAverage = sumOfClassGrades / numStudents
# math classAverage = sumOfClassGrades / numStudents

# create Function3  (convert_to_letter_grade(numericScore))  that will get average letter grade for the class
# f3 is the return
    return (classAverage, convert_to_letter_grade(classAverage))


# create function 4: main() function:  will  prompts to enter the number of students in the course and then a loop that will prompt the user to enter each students grade, calculate a running total of the students’ scores, call the appropriate functions listed above, 

def main():
    numStudents = int(input("Please enter the number of students in your " + courseName + " course:"))
    sumOfClassGrades = 0
    for i in range(numStudents):
        grade = int(input(f"Please enter the grade for student {i+1}: "))
        sumOfClassGrades += grade
        letterGrade = convert_to_letter_grade(grade)
        print(f"Student {i+1} received a {letterGrade} {grade}")
   
    

    classAverage, classLetterGrade = compute_class_average(numStudents, sumOfClassGrades)
    print(f"\nClass average is {classAverage} ({classLetterGrade})")
    if classAverage >= 75:
        print("Great job lesson planning. Give the students a little reward.")
    else:
        print("Not great, lesson plan improvement is needed.")

'''    
if class average is bad: print == print("Not great, lesson plan can be improved.")
 
if class average is good: print
print("Great job lesson planning! Give the students a little reward.")
    '''

if __name__ == "__main__":
    main()

 
#Define student's id 