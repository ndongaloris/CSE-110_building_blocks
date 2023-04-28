import random

print("\nWelcome to the wordle game!!\n")
count = 0


def counts():
    if count > 4:
        print(f"you have {5 - count} guess left ")
    else:
        print(f"you have {5 - count} guesses left ")


secret_words = ["Heaven", "Temple", "Bible", "Christ"]
secret_word = random.choice(secret_words).lower()


def print_hint():
    print("Your hint is :", end="")
    for i in secret_word:
        print("_ ", end="")
    print()


print_hint()
guess_word = input("What is your guess?: ").lower()
count += 1


def general_hint():
    print("Your hint is : ", end="")
    for i in range(len(guess_word)):
        letter = guess_word[i]
        if letter == secret_word[i]:
            print(letter.upper(), end="")
        elif letter in secret_word[i]:
            print(letter.lower(), end="")
        else:
            print("_ ", end="")
    print()


while count < 5 and guess_word != secret_word:
    if len(secret_word) != len(guess_word):
        print("Your guess was not correct.")
        print(
            "Sorry, the guess must have the same number of letters as the secret word."
        )
        guess_word = input("\nWhat is your guess?: ").lower()
        count += 1
        counts()
    else:
        general_hint()
        guess_word = input("\nWhat is your guess?: ").lower()
        count += 1
        counts()
if secret_word == guess_word:
    print("Congratulations! You guessed it!")
else:
    print("Try again, next time.")
if count > 1:
    print(f"It took you {count} guesses ")
else:
    print(f"It took you {count} guess ")
