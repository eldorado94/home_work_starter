import math

print('Input just one number for func y = f(x), where x is: ')
num = float(input())

if -math.pi <= num <= math.pi:
    y = (math.cos(3 * num))
    print("The answer its: ", y)
elif num < -math.pi or num > math.pi:
    y = num
    print("The answer its: ", y)
else:
    print("Unexpected error!")