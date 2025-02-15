'''
8. Graduation 
Write a program that calculates the student's average grade from all of his/her studies. On the first line, you will receive the student's name and on each following line his/her annual grades. The student passes to the next grade if his annual grade is greater than or equal to 4.00. If he/she failed more than once, he/she will be excluded and the program ends, printing the student's name and the class he/she was excluded from.
 At the successful completion of grade 12 to be printed: 
"{student's name} graduated. Average grade: {average grade of all studies}"
In the student is excluded from school, to be printed:
"{student's name} has been excluded at {class he/she was excluded from} grade"
The average grade must be formatted to two digits after the decimal point. 
'''
student_name = input()

sum_grade = 0.00
student_class = 1
fail_exam = 0

while True:
    grade = float(input())
    if grade < 4.00:
        fail_exam +=1
        if fail_exam > 1:
            # student je pao godinu
            print(f"{student_name} has been excluded at {student_class} grade")
            break
    else:
        student_class += 1
        if student_class > 12:
            # student je diplomirao
            student_class = 12
            sum_grade += grade
            print(f"{student_name} graduated. Average grade: {(sum_grade / student_class):.2f}")
            break
        sum_grade += grade