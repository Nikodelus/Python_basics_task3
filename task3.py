import random


s = input('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach')

min = int(0)
max = int(1000)

ans = '0'
while ans != 'you win':
    a = 'lier'
    guess = int((max - min) / 2) + min
    while a == 'lier':
        print(f'Zgaduję: {guess}')
        ans = input('Am I right? ')
        if ans == 'you win':
            print('Computer won!')
            break
        elif guess == min or guess == max:
            print("You lied to me!")
            a = 'lier'
            break
        elif ans == 'too big':
            max = guess
            a = '0'
        elif ans == 'too small':
            min = guess
            a = '0'
