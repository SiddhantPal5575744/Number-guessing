import random

list=[1,2,3,4,5,6,7,8,9,10]
rand=(random.choice(list))

chances=5
#while chances>0:
user=int(input("Guess a number"))

while chances>0:
    if(user<rand):
        print("the number is greater thann your chosen number")
        chances=chances-1
        user=int(input("Guess a number"))
    elif(user>rand):
        print("the number is smaller than your chosen number")
        chances=chances-1
        user=int(input("Guess a number"))
    else:
        print("YOU WON")