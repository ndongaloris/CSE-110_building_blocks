import random
#need to fix it, it gernerates the same number over and over in the while loop, so when you say yes, the number is still the same.
print()
magic_number = random.randint(1,100)
# magic_number = 100
play='yes'
guess_number = int(input('What is your guess?: '))
count = 1
while play == 'yes':
    if magic_number > guess_number:
        print('Higher')
        count += 1
        guess_number = int(input('What is your guess?: '))
    elif magic_number < guess_number:
        print('Lower')
        count += 1
        guess_number = int(input('What is your guess?: '))
    else:
        print('You guessed it, Congrats!\n')
        if count <= 1:
            print(f'It took you {count} guess')
        else:
            print(f'It took you {count} guesses')
        play = input('Do you want to play again?').lower()
        if play == 'yes':
            guess_number = int(input('What is your guess?: '))
        else:
            print('Thanks for playing, see you later!!')
