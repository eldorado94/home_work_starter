print('Введите число a (любое одно)')
value_a: int = input()  # ввод первого числа

print('Введите число b (любое одно)')
value_b: int = input()  # ввод второго числа

print('Введите число c (любое одно)')
value_c: int = input()  # ввод третьего числа

if value_a <= value_b and value_b <= value_c:  # сравнение чисел bи вывод резутата
    print("True")
else:
    print("False")