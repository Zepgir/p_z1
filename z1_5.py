## 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers()
print("Введите координаты точки В")
pointB = inputNumbers()
print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}