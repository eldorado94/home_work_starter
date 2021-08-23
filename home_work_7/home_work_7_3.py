def main():
    text = list(map(str, input('Введите любой текст (слова писать через пробел) : ').split()))
    print('Текст без правок-: ', text)
    print('Текст по алфавиту: ', sorted(text, key=str.lower))
main()