#! python3

import time, threading, random


print('''Thanks for playing the Alphabet Game.
         The rules are quite simple.
         1. The program will select a letter.
         2. Enter as many words that start with that letter within 20 seconds.
         3. The game will repeat this process until every letter of the alphabet is given.
         4. Once the program ends, your results will be displayed.
            * To leave the program enter CTRL + Z *
            That's all and good luck!
         ''')

letter = ['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U','V',
               'W','X','Y','Z']


def letterGiver():
    n = 0
    while n < 26:
        print("Enter as many words as you can that start with: " + letter[n])
        time.sleep(.1)
        n += 1
        userWords = []
        if n == 26:
            break

def execution():
    i = 1
    for i in range(1):
        letterGiver()
        name = input()
        userWords = userWords + [name]

execution()
