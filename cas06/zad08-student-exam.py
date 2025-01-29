'''
8. On Time for the Exam
A student must go to an exam at a certain time. He arrives at the examination room at a certain time of arrival. It is considered that the student arrived on time if he arrives at the time of the exam or up to half an hour before. If he arrives more than 30 minutes earlier, he is early. If he comes after the exam time, he is late. Write a program that reads exam time and arrival time and records whether the student arrived on time, is early or late, and by how many hours or minutes is early or late.
'''
hours_exam = int(input())
minutes_exam = int(input())
hours_arrival = int(input())
minutes_arrival = int(input())

sum_min_exam = hours_exam * 60 + minutes_exam
sum_min_arrival = hours_arrival * 60 + minutes_arrival

if(sum_min_arrival > sum_min_exam):
    # zakasnili na ispit
    print("Late")
    diff_time = sum_min_arrival - sum_min_exam
    # izracunati sate i minute od ukupnog vremena
    # hours = diff_time // 60; minutes = diff_time % 60;
    hours = diff_time // 60
    minutes = diff_time % 60
    if hours == 0:
        print(f'{minutes} minutes after the start')
    else:
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')

# u else grani sum_min_exam >= sum_min_arrival
# 8:40 8:30 => 8*60+40 = 520 i 8*60+30 = 510
elif (sum_min_exam - sum_min_arrival <= 30):
    # na vreme
    print("On Time")
    if(sum_min_exam != sum_min_arrival):
        diff_time = sum_min_exam - sum_min_arrival

        hours = diff_time // 60
        minutes = diff_time % 60

        if hours == 0:
            print(f'{minutes} minutes before the start')
        else:
            if minutes < 10:
                print(f'{hours}:0{minutes} hours before the start')
            else:
                print(f'{hours}:{minutes} hours before the start')
else:
    print("Early")
    diff_time = sum_min_exam - sum_min_arrival

    hours = diff_time // 60
    minutes = diff_time % 60

    if hours == 0:
        print(f'{minutes} minutes before the start')
    else:
        if minutes < 10:
            print(f'{hours}:0{minutes} hours before the start')
        else:
            print(f'{hours}:{minutes} hours before the start')