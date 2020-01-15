from pytictoc import TicToc
import time, threading, random
from spellchecker import SpellChecker


t = TicToc() #create instance of class

letters = ['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U','V',
               'W','X','Y','Z']
userWords = []
n = 0



while n < 26:
    t.tic()
    print('Enter words that start with the letter: ' + letters[n])
    name = input("")
    userWords = userWords + [name]
    t.toc()
    n += 1
    if n == '':
        break
    if n == 26:
        break



#Results
print('Of the %s amount of words:' % len(userWords))

userDictionary = dict(zip(letters, userWords))
print(userDictionary)

spell = SpellChecker()
misspelled = spell.unknown(userWords)

print('you misspelled %s words' % len(misspelled))
userWords.pop()
