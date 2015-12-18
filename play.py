import random
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def printc(text):
    clear()
    print(text)
printc("Hello!")
input()
printc("I'm mothebad!")
input()
printc("Type a number between 1 and 10")
input()
randomnum=-1
while randomnum<0 or randomnum>10:
    randomnum=int(input())
guess=random.randint(1,10)
if randomnum==guess:
    print("You guessed it! :-)")
else:
    print("You failed :-(")