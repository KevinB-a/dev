import math
#exercise1 : a chessboard
white=" # # # # # # # #"
black="# # # # # # # #"
space="   "
print(space + '"')
for i in range(1,9): # use loop for
    if i % 2==0:
        print(space + black) #when i is even print the variable black
    else :
        print(space + white)#when i is not even print the variable white
print(space + '"')
#exercise2 : Matrix in the terminal
suite="1000 0100 0010 0001 "
dashes='"-------"'
for i,j in enumerate(suite): #the function enumerate use a count for display every element
    if i% 5==4:
        print(dashes) #dislay dashes in every five lines
    else:
        print(j)

#exercise3 : even number ?
def even(number):# create a function who display true if the number is even or display false if it's not even
   if number % 2==0:
       print("true")
   else:
       print("false")
even(0)
#exercise4 : you say factorial ?
def factorial(n): # create function that calculate the factorial of a number
    if n==0:
        return 1 # here i return 1 because factorial 0 =1
    else:
        return n*factorial(n-1)# remind the function until he find the result
print(factorial(5))

#exercise5 :the dashes count
def replace(text):
    """create a function who replace a character by an another one"""
    text=text.replace("-","\_")  #replace() permit to change a str"""
    print(text)
    if text=="":
        print("you write nothing")  #error message when user press enter when computer ask something"""
text=input("please enter your sentence")
replace(text)
#exercise6 : train with the boards
shopping_list=["tomatoes","apples","strawberry","pinapple","blueberry"]  #create a list"""
print(shopping_list[0])
print(shopping_list[-1])
length=int(len(shopping_list)/2) #calculate the middle of the list """
print(shopping_list[length])
#exercise7 : man's board
man=[["billet"," kevin"," 27"," 20/12/1991"],["toto"," titi"," 17"," 30/02/2002"],["tata"," tito"," 34"," 01/03/1985"]]
def infos(man): # display every elements of the lists  """
    for i in range(len(man)): #the value of i change it begin at 0 until 2 here (3 lists on the list man)
        for j in range(len(man[i])): #the value of j change it begin at 0 until 3 (every list content 4 elements)
            print(man[i][j], end='')
        print()
infos(man)
#exercise8 : the max of a board
list_of_numbers=[112,67,193,57,98]
liste=["appartement","velo","couac","debit","envelloppe"]
print(max(list_of_numbers))
def maxi(liste):
    try: #try to execute print
        print(max(liste))
    except: #if error find display the erro message
        print("error message: you put differents types in your list")
maxi(liste2)

#exercise9 : To Do list
todolist=[]
task=""   #create empty variable for continue in while loop
while task !="fin": #while loop continue until user insert fin
    task=input("enter a task")
    if task=="fin":
        print(todolist) #display elements in todolist
    todolist.append(task) #todolist.append() add element in todolist
