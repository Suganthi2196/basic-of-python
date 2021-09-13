pizza=input("select the type of pizza you want \n1-small pizza\n2-medium pizza\n3-large pizza")
bill=0
if pizza=="1":
    bill+=30
elif pizza=="2":
    bill+=40
else:
    bill+=50
print(f"your bill is {bill}")
pepper_onion=input("if you want to pepper onion select \nyes\nno")
if pizza=="1" and pepper_onion=="yes":
    bill+=10
elif pizza=="2" and pepper_onion=="yes":
    bill+=30
else:
    bill=bill
print(bill)