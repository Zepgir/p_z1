## 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 



def InputNumbers(inputText):
    proverka = False
    while not proverka:
        try:
            number = int(input(f"{inputText}"))
            proverka = True
        except ValueError:
            print("Введите число")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Это выходной")
    elif 0 < num < 6:
        print("Это будний день")
    else:
        print("Введите число от 1 до 7 включительно")


num = InputNumbers("Введите число: ")
checkNumber(num)