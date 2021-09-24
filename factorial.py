n=int(input("Enter the input value"))
i=1
mul=1
while n>=i:
    print(n, end="x")
    mul=mul*n
    n=n-1
print(f"{n}={mul}")
