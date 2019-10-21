#exercise1 : a chessboard
white=" # # # # # # # #"
black="# # # # # # # #"
space="   "

for i in range(1,9):
    if i % 2==0:
        print(space+black)
    else :
        print(space+white)
