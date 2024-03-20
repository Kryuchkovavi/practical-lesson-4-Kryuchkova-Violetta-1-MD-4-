def z1():
    a = int(input("Введите число: "))
    if a%3 == 0:
        print("число делится на 3")
    else:
        print("число не делится на 3")

def z2():
    try:
        a = int(input("Введите число: "))
        if 100%a == 0:
            print("100 делится на", a)
        else:
            print("100 не делится на", a)
    except ZeroDivisionError:
        print("Ошибка, деление на ноль!")
    except ValueError:
        print("Ошибка, вы ввели строку!")

def z3():
    a = input("Введите дату: ")
    b = a.split(sep= '.')
    c = (b[2])
    d = (c[2])+(c[3])
    if int(b[0]) * int(b[1]) == int(d):
        print("True")
    else:
        print("False")

def z4():
    try:
        a = input("Введите число: ")
        if len(a) == 6:
            if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
                print("Счастливое число")
            else:
                print("Несчастливое число")
        else:
            print("Ошибка, введите число из шести цифр")
    except ValueError:
        print("Ошибка, используйте цифры")

z4()