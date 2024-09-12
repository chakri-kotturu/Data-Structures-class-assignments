import time
import resource 
cur=time.time_ns()

student_grades = [85, 92, 78, 90, 88, 76, 95, 89, 73, 91]

def find_highest_grade(grades):
    highest_grade = grades[0]
    lowest_grade = grades[0]
    for grade in student_grades:
        if grade > highest_grade:
            highest_grade = grade
        elif grade < lowest_grade:
            lowest_grade = grade
    return [highest_grade,lowest_grade]

highest_and_lowest_grade = find_highest_grade(student_grades)
print("The highest grade is:", highest_and_lowest_grade[0])
print("The lowest grade is:", highest_and_lowest_grade[1])


cur2=time.time_ns()
print("time cost in milliseconds :",(cur2-cur)/1000)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
print ("memory cost: %5.1f KByte" % (memMb))