'''
2. Exam Preparation
Write a program with which Michael solves problems from his exams until he receives the "Enough" command from his lecturer. For each problem he solves, he receives a grade. The program should finish when receiving the "Enough" command or if Michael receives the specified number of poor grades.
A poor grade is any grade that is less than or equal to 4.
'''
poor_grades_number = int(input())

failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < poor_grades_number:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {(grades_sum / solved_problems_count):.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")