#exercise1 :the bigger number
import math
number=1
number1=2
number2=3
number3=4
if number>number1 and number>number2 and number>number3:    #compare number with other variable
    print("le nombre le plus grand est ",number)
elif number1>number and number1>number2 and number1>number3: #compare number1 with other variable
    print("le nombre le plus grand est",number1)
elif number2>number and number2>number1 and number2>number3: #compare number2 with other variable
    print("le nombre le plus grand est ",number2)
else:
    print("le nombre le plus grand est",number3) # if other condition are false display last variable


#exercise2 : age condition
try:
    age=int(input("please enter your age"))
except ValueError:
    print("you did not write anything")hide_number=int(input("please enter a number"))
if age<0:
    print("please enter a real age")
elif math.sqrt(age).is_integer():
    print("you age is a perfect square")
if age>= 21:
    print("you have access ")
if age % 2==0:
    print("your age is an even number")
else:
    print("you age is not a perfect square")

#exercise3 : Hide number
hide_number=int(input("please enter a number"))
guess_number=int(input("please enter a number"))
while guess_number!=hide_number :
    if guess_number<hide_number:
        print("enter a bigger number")
        guess_number=int(input("please enter a number"))
    if guess_number>hide_number:
        print("enter a little number")
        guess_number=int(input("please enter a number"))
pass
print("you win, you find the hide number")

# exercise4 : number in loop
n=0
while n!=100:
    n=n+1
    print(n)
