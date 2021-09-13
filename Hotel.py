option=int(input("Enter the option \n1-VEG\n2-NON_VEG"))
if option==1:
    dishes=input("enter the dishes type \n1-breakfast\n2-lunch")
    if dishes=="1":
        varities=input("enter the variable type\n1-idly------Rs.6\n2-pongal----Rs.20")
        print(f"{varities} coming soon")
    elif dishes=="2":
        varities=input("Enter the varities types \n1-sambar-----Rs.40 \n2-curd------Rs.30")
        print(f"{varities} comming soon")
elif option==2:
    dishes = input("enter the dishes type \n1-breakfast\n2-lunch")
    if dishes=="1":
       varities=input("enter the option \n1-chilly idly\n2-paroota")
       print(f"{varities} comming soon")
    elif dishes=="2":
       varities=input("enter the varities \n1-briyani----Rs.200\n2-meals----Rs.100")
       print(f"{varities} comming soon")
else:
       print("Invalid")