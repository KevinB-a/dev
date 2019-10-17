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
