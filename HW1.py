'''1. Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

"""start = int(input('Введите число от 1 до 7: '))
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
    print("Вы ввели не верное число, повторите ввод.")"""

"""2. Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.""" 


"""print ('x y z')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if (not ((x) or (y) or (z))) == (not (x) and not (y) and not (z)):
                print(x,y,z)"""



""" 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится) (скобка не нужна это бред получаеться)
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3"""  

"""x = int(input("x = "))
y = int(input("y = "))
if x > 0 and y > 0:
    print("1-я четверть")
elif x < 0 and y > 0:
    print("2-я четверть")  
elif x < 0 and y < 0:
    print("3-я четверть")
elif x > 0 and y < 0:
        print("4-я четверть")"""


""" 4. Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y)."""


"""x = int(input("Введите нужную четверть "))
if x == 1:
    print("координата х = от 0 до бесконечности, координата y = от 0 до бесконесности")
elif x == 2:
    print("координата х = от 0 до минус бесконечности, координата y = от 0 до бесконесности")
elif x == 3:
     print("координата х = от 0 до минус бесконечности, координата y = от 0 до минус бесконесности")
elif x == 4:
    print("координата х = от 0 до  бесконечности, координата y = от 0 до минус бесконесности")
else:
    print("Нет такого значения четверти")"""


""" 5. Напишите программу, которая принимает на вход координаты двух точек и 
находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""


'''Xa = float(input("Введите координату Х 1го числа "))
Xb = float(input("Введите координату Y 1го числа "))
Ya = float(input("Введите координату X 2го числа "))
Yb = float(input("Введите координату Y 2го числа "))
print(f"Введенные вами координаты точки А({Xa}, {Xb}) и точки B({Ya}, {Yb})")
import math
distance = math.sqrt(((Ya-Xa)**2)+((Yb-Xb)**2))
print(distance)'''