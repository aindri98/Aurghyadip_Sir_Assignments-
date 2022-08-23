n=int(input("Enter a positive integer:"))
while n!=1:
    if(n%2==0):
        print(f"{n} ", end="")
        n=n//2
    else:
        print(f"{n} ", end="")
        n = (n * 3) + 1
else:
    print("1")
    