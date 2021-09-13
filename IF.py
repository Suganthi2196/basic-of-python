a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=(input("Enter the operand:"))
if c=="+":
    print(f"{a}+{b}={c}")
elif c=="-":
    print(f"{a}-{b}={c}")
elif c=="*":
    print(f"{a}*{b}={c}")
elif c=="/":
    print(f"{a}/{b}={c}")
else:
    print("Invalid oerator")
