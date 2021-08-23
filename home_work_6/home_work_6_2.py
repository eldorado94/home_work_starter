def checkFunc():

    string_to_check = input("Введите фразу :")

    if string_to_check == string_to_check[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")

checkFunc()