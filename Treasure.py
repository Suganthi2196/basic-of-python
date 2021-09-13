print("welcome to the treasure")
option=input("Where do you want to go \n1-left\n2-right")
if option=="1":
    a=input("welcome to island \n1-swim\n2-not")
    if a=="1":
        print("Gameover")
    else:
        b=input("choose color \n1-yellow\n2-red")
        if b=="1":
            print("reached")
        else:print("Gameover")
else:
    print("Gameover")