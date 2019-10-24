"""
def maxi(liste):
    liste=[1,8,78,54,32]
    for i in liste:
        if isinstance(liste[i], int):
            print(max(liste))
        elif isinstance(liste[i], str):
            print(max(liste))
        else:
            print("you put str and int in the same list")
liste=[1,3,5,7,9]
maxi(liste)"""
"""liste=["r","didou","jack","mich","coucou",8]
for i in range(0,len(liste)):
    if isinstance(liste[i], int) and not isinstance(liste[i],str):
        print(liste[i])
    elif isinstance(liste[i],str) and not isinstance(liste[i], int):
        print(liste[i])
    else:
        print("you put str and int in the same list")"""

todolist=[]
task=""
while task !="fin":
    task=input("enter a task")
    todolist.append(task)
print(todolist)
