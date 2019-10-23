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
def replace(text):
    """create a function who replace a character by an another one"""
    text=text.replace("-","\_")
    print(text)
    if text=="":
        print("you write nothing")
text=input("please enter your sentence")
replace(text)
#exercise6 : train with the boards
shopping_list=["tomatoes","apples","strawberry","pinapple","blueberry"]
print(shopping_list[0])
print(shopping_list[-1])
length=int(len(shopping_list)/2)
print(shopping_list[length])
#exercise7 : man's board
man=[["billet"," kevin"," 27"," 20/12/1991"],["toto"," titi"," 17"," 30/02/2002"],["tata"," tito"," 34"," 01/03/1985"]]
def infos(man):
    for i in range(len(man)):
        for j in range(len(man[i])):
            print(man[i][j], end='')
        print()
infos(man)
