


while True:

    a = int(input('Сумма кредита: '))
    
    if a >= 50000:

        b = a * (3.47/100)

        print(round(b,2))
        break

    else: 
        print('Сумма займа должна быть не меньше 50000')

