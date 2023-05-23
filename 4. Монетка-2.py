import math

x = float(input("Введите  координату х: "))
y = float(input("Введите  координату y: "))
r = float(input("Введите  радиус r: "))

if math.sqrt(x ** 2 + y ** 2) < r:
    print('Монетка где-то рядом!')
else:
    print("Монетки в области нет!")