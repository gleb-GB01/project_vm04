# HW1
#number = int(input('Введите число: '))
#print(number + 2)

# HW2
#number = int(input('Введите число от 0 до 10 (не включительно): '))
#while 10 < number > 0:
#    print('Введено не верное число')
#    number = int(input('Введите число от 0 до 10 (не включительно): '))
#else:
#    print(number ** 2)

# HW3

name = 'Вася'
sur_name = 'пупкин'
age = int(input('Введите Возраст: '))
veight = int(input('Введите Вес: '))
if age <= 30 and 50 <= veight < 120:
    print(name, age, 'год, ', 'вес', veight, '- Вы в хорошем состоянии')
elif age > 30 and 50 > veight > 120:
    print(name, age, 'год, ', 'вес', veight, '- Вам следует заняться собой')
elif age > 40 and 50 <= veight < 120:
    print(name, age, 'год, ', 'вес', veight, '- Вам требуется врачебный осмотр')






