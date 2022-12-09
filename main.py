def naob(x):
    y = 0
    count = 0
    while x >= 10:
        x /= 10
        count += 1
    print (x)
    for i in range(count+1):
        y += (x//1)*10**i
        x -= x//1
        x *= 10
        if abs(round(x) - x) < 0.0000001:
            x = round(x)
    return int(y)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

a_n = naob(a)
b_n = naob(b)
print('Проверка появления строки в GIT')
print("Первое число наоборот:", a_n)
print("Второе число наоборот:", b_n )

print ("Сумма (проверка):", a_n + b_n)
print("Сумма наоборот (проверка):", naob(a_n + b_n))



