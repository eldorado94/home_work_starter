
def main():

    while name is not None:
        name = str(input('Please, enter you name: '))

        if name:
            print('Hello ', name, '!')
            continue
        else:
            name = 'Eldar'  # без объявления этой переменной не работает как надо
            print('Hello ', name, '!')

main()
