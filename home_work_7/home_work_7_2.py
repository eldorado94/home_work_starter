
def main():
    characters = list(map(int, input('Введите значения цен через пробел : ').split()))
    print(characters)
    print('Наибольший элемент списка :', max(characters))
    print('Наименьший элемент списка :', min(characters))
    print('Сумма всех элементов списка :', sum(characters))
    middle = float(sum(characters))/len(characters)
    print('Сумма всех элементов списка :', middle)
main()
