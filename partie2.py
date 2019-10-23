import math
#exercise1 : a chessboard
white=" # # # # # # # #"
black="# # # # # # # #"
space="   "
print(space + '"')
for i in range(1,9):
    if i % 2==0:
        print(space + black)
    else :
        print(space + white)
print(space + '"')
#exercise2 : Matrix in the terminal
suite="1000 0100 0010 0001 "
dashes='"-------"'
for i,j in enumerate(suite):
    if i% 5==4:
        print(dashes)
    else:
        print(j)

#exercise3 : even number ?
def even(number):
   if number % 2==0:
       print("true")
   else:
       print("false")
even(138)
#exercise4 : you say factorial ?
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#exercise5 :the dashes count
text=input("please enter your sentence")
def replace():
    """create a function who replace a character by an another one"""
    text1=text.replace("-","\_")
    print(text1)
    if text=="":
        print("you write nothing")

replace()
#exercise6 : train with the boards
shopping_list=["tomatoes","apples","strawberry","pinapple","blueberry"]
print(shopping_list[0])
print(shopping_list[-1])
length=int(len(shopping_list)/2)
print(shopping_list[length])
