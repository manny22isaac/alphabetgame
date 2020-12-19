#! python3
# Prints letter of the alphabet
import time

print('''Thanks for playing the Alphabet Game.
         The rules are quite simple.
         1. The program will select a letter.
         2. Enter as many words that start with that letter within 5 seconds.
         3. The game will repeat this process until every letter of the alphabet is given.
         4. Once the program ends, your results will be displayed.
            * To leave the program enter CTRL + Z *
            That's all and good luck!
         ''')


letters = ['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U','V',
               'W','X','Y','Z']
userWords = []



def timer():
    t_end = time.time() + 5
    while time.time() < t_end:
        name = str(input('Input Data :'))
        userWords.append(name)
        
def repeator():
    n = 0
    while n < 26:
        print('Enter words that start with the letter: ' + letters[n])
        timer()
        n += 1


start = input("Ready? Type Y/N: ").upper()

if start == "Y":
        repeator()
else:
    print("Oh that's too bad. So Long!")
    quit()


print('You have created %s words:' % len(userWords))
for name in userWords:
    print('  ' + name)

