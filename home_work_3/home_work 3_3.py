import math

print('Привет! Я твой калькулятор и постараюсь посчитать все)')

print("Какую операцию вы хотите выполнить? Введите число напротив операции \n 1 Сложение \n 2 Вычитание \n 3 Деление"
      "\n 4 Умножение \n 5 Возведение  в  степень \n 6 Синус \n 7 Косинус \n 8 Тангенс ")

oper = int(input())

if oper < 4:
    if oper == 1:
        print('Введите первое число: ')
        num_1 = float(input())
        print('Введите второе число: ')
        num_2 = float(input())
        result = num_1 + num_2
        temp = 'сложения'
    elif oper == 2:
        print('Введите первое число: ')
        num_1 = float(input())
        print('Введите второе число: ')
        num_2 = float(input())
        result = num_1 - num_2
        temp = 'вычитания'
    elif oper == 3:
        print('Введите первое число: ')
        num_1 = float(input())
        print('Введите второе число: ')
        num_2 = float(input())
        result = float(num_1 / num_2)
        temp = 'деления'
    elif oper == 4:
        print('Введите первое число: ')
        num_1 = float(input())
        print('Введите второе число: ')
        num_2 = float(input())
        result = num_1 * num_2
        temp = 'умножения'
elif oper == 5:
    print('Введите число: ')
    num_1 = float(input())
    print('Введите степень числа: ')
    result = num_1 ** num_2
    temp = 'возведения в степень'
elif oper > 5:
    if oper == 6:
        print('Введите число: ')
        num_1 = float(input())
        result = math.sin(num_1)
        temp = 'синуса числа'
    elif oper == 7:
        print('Введите число: ')
        num_1 = float(input())
        result = math.cos(num_1)
        temp = 'косинуса числа'
    elif oper == 8:
        print('Введите число: ')
        num_1 = float(input())
        result = math.tan(num_1)
        temp = 'тангенса числа'
else:
    print('Вы ввели неверное значение!')
print ('Результат ',temp,' = ',result)