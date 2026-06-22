def grad_calculator(marks):
    if marks >= 90:
        return 'A','Excellent work! keep it up'
    elif marks >= 80:
        return'B','Very good! You are doing great'
    elif marks >= 70:
        return'C','Good effort! Keep improving'
    elif marks >= 60:
        return'Grade D','keep doing! You can do better'
    else:
        return'F','Dont give up! Do hard work'
       

std_name = input('enter the student name : ')

while True:
    marks = float(input('enter the student marks = '))

    if 0 <= marks <= 100:
       break
    else:
        print('Something went wrong! give input btw (0-100)')

std_grade, msg_to_std = grad_calculator(marks)

print('\n-------Result-------')
print('Student name:',std_name )
print('Marks :',marks)
print('Geade :',std_grade)
print(f'{msg_to_std}----\n')

