import time

letters = ['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U','V',
               'W','X','Y','Z']
userWords = []
n = 0
while n < 26:
    print('Enter words that start with the letter:' + letters[n])
    n += 1
    name = input()
    userWords = userWords + [name]
    if n == '':
        break
    if n == 26:
        continue


#Results
print('You have created this amount of words:')
for name in userWords:
    print('  ' + name)


userDictionary = dict(zip(letters, userWords))
print(userDictionary)
