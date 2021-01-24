import random


s = input('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach')

min = int(0)
max = int(1000)

ans = '0'
while ans != 'you win':
        guess = int((max - min) / 2) + min
        print(f'Zgaduję: {guess}')
        ans = input('Am I right? ')
        if ans == 'you win':
            print('Computer won!')
            break
        elif guess == min or guess == max:
            print("You lied to me!")
            break
        elif ans == 'too big':
            max = guess
        elif ans == 'too small':
            min = guess
