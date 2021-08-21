def addition(temp='сложения'):
    num_1 = float(input(print('Введите первое число: ')))
    num_2 = float(input(print('Введите второе число: ')))
    result = num_1 + num_2
    print('Результат', temp, 'равен :',result)
def substraction(temp='вычитания'):
    num_1 = float(input(print('Введите первое число: ')))
    num_2 = float(input(print('Введите второе число: ')))
    result = num_1 - num_2
    print('Результат', temp, 'равен :',result)

def division(temp='деления'):
    num_1 = float(input(print('Введите первое число: ')))
    num_2 = float(input(print('Введите второе число: ')))
    if not num_1 and num_2 != 0:
        print('нА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!')
    else:
        result = float(num_1 / num_2)
        print('Результат', temp, 'равен :',result)

def multiplication(temp='умножения'):
    num_1 = float(input(print('Введите первое число: ')))
    num_2 = float(input(print('Введите второе число: ')))
    result = num_1 * num_2
    print('Результат', temp, 'равен :',result)

def result_out():
    print('Вы ввели неверное значение!')

def main():
    print('Привет! Я твой калькулятор и постараюсь посчитать все)')

    print("Какую операцию вы хотите выполнить? Введите число напротив операции "
        "\n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение")
    oper = int(input())
    if oper == 1:
        addition()

    elif oper == 2:
        substraction()

    elif oper == 3:
        division()

    elif oper == 4:
        multiplication()

    else:
        result_out()

main()  # main function
