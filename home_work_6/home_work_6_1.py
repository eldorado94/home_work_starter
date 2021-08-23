value = 5

def multi():
    global value
    value = value * 3
    print("Значение в функции:", value)

multi()
print("Значение вне функции:", value)
