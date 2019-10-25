todolist=[]
task=""   #create empty variable for continue in while loop
while task !="fin": #while loop continue until user insert fin
    task=input("enter a task")
    if task=="fin":
        print(todolist) #display elements in todolist
    todolist.append(task) #todolist.append() add element in todolist
