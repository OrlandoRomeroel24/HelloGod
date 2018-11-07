'''
docu
'''


import random
secret = random.randint(1,99)
guess = 0
tries = 0
print('Can You Guess my Number')
print('My number is a interger')
while guess != secret and tries < 6 :
    print('Hey what is your guess?')
    guess = int(input())
    if guess < secret :
        print('Too Low')
    elif guess > secret :
        print('Too High')
        tries = tries + 1
if guess == secret :
    print('You are correct Bravo!')
else :
    print('No more guesses')
    print('The secret number was : ',secret)

