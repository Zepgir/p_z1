## 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        checker = False
        while not checker:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                checker = True
            except ValueError:
                print("Введите целое число")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")