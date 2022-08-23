from this import d


n=int(input("Enter the number:"))
if n>2:
    f=2
    while (f<=n):
        if(n%f==0):
            print(f)
            n=n//f
        else:
            f=f+1
else:
    print("The number entered is less than 2")
    
        
    