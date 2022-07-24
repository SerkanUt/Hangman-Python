import random
from words import words
import string


def rand_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    word = word.upper()
    return word


def hangman():
    word = rand_word(words)

    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = []
    sc = len(word) * '_/'
    screen = list(sc.split('/'))
    screen.remove('')
    guesses = 0
    lives = 5
    while lives > 0 and '_' in screen:
        print('Total Guesses: ', guesses)
        print('remaining lives: ', lives)
        print('Used Letters: ', used_letters)
        print(screen)
        guess = game()

        if guess in screen:
            print('You have Already Guessed That Letter')
        elif guess in letters:
            used_letters.append(guess)
            index = indexes(word, guess)
            i = len(index)
            guesses += 1
            while i > 0:
                screen[index[i - 1]] = f'{guess}'
                i -= 1
        else:
            used_letters.append(guess)
            print('You guessed Wrong')
            guesses += 1
            lives -= 1
    if lives == 0:
        print('Total Number Of Guesses: ', guesses)
        print('the word was: ', word)
        return ('You Lose!')

    print('Total Number Of Guesses: ', guesses)
    print('the word was: ', word)
    return ('You Won!')


def game():
    user = input('Guess An Uppercase Character: ')
    return user


def indexes(word, guess):
    index = []
    t = -1
    while t > -2:
        try:
            t = word.index(guess, t + 1)
            index.append(t)
        except ValueError:
            break

    return index


print(hangman())
