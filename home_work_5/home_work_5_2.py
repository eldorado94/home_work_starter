def main(a=6, b=24):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    nod = a + b
    return print('Наибольший общий делитель переданных чисел в параметры :',nod)

main()