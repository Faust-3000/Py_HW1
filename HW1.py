'''Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

start = int(input('Введите число от 1 до 7: '))
if start == 1:
    print("Нет это Понедельник" )
elif start == 2:
    print("Нет это Вторник ")
elif start == 3:
    print("Нет это Среда ")   
elif start == 4:
    print("Нет это Четверг ")
elif start == 5:
    print("Нет это Пятница ")
elif start == 6:
    print("Да это Суббота, выходной!!!! ") 
elif start == 7:
    print("Да это Воскресенье, выходной!!! ")
else:
    print("Вы ввели не верное число, повторите ввод.")