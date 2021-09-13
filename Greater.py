a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if a>b:
    if a>c:
        print(f"a is greater")
    else:
        print(f"c is greater")
else:
    if b>c:
        print(f"b is greater")
    else:
        print(f"c  is greater")