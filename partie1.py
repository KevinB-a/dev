import math
from math import pi
#exercise1 :the bigger number
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
try:                                        """i use a try for create an except """
    age=int(input("please enter your age"))
except ValueError:                          """if user enter something else than an integer an error message is display """
    print("you did not write anything")
if age<0:
    print("please enter a real age")
elif math.sqrt(age).is_integer():           """sqrt is a math function who calculate square root of a number """
    print("you age is a perfect square")    """is_integer verify if number is an integer or not if that is the
if age>= 21:                                   case display true and if not display False"""
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
n=0 """initialize n"""
while n!=100:   """i use while loop """
    n=n+1       """ don't forget increment if you not put this increment your loop is infinite"""
    print(n)

# exercise5 : number in loop second part
n=0
while n!=100:
    n=n+1
    if n % 2==0: """display only even numbers """
        print(n)

#exercise6 : fill the pool
def filling(length,width,depth,debit): """create a function filling who calculate the filling time """
    m3=(length*width*depth)/debit
    print("you fill the pool in" ,m3,"minutes")
filling(3,4,2,3)

#exercise7 : area and perimeter of circle
r=int(input("please enter ray of the circle in cm"))
def area_circle():
    area=round(pi*(r**2),2)"""create area_circle who display the result of area"""
    print(area)
def perimeter_circle():
    perimeter=round(2*pi*r,2)   """create perimeter_circle who display the result of perimeter """
    print(perimeter)
area_circle()
perimeter_circle()

#exercise8 : a pyramid
n=0
symbol="*"
while n!=6:         """here the while loop permit display every iterations of the loop """
    print(n*symbol)
    n=n+1

#exercise9 : FIZZ BUZZ
number=0
while number!=100:
    if (number/3).is_integer() and (number/5).is_integer():
        print("FIZZBUZZ")
    if (number/3).is_integer() and not (number/5).is_integer(): """he verify if these condition a good,
        print("FIZZ")                                              if it that case display this message """
    if (number/5).is_integer() and not (number/3).is_integer():
        print("BUZZ")
    number=number+1
