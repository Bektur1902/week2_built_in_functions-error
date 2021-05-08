# Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел

count = 0
a = []

while count < 5:
    
    x = int(input('Enter number: '))
    a.append(x)
    b = set(a)
    count += 1

print('Самое маленькое число: ', min(b))

