def prove_pascal(n,d,n1,d1):
    if((n*d1==n1*d)):
        print("pascal's principle proved")
    else:
        print("pascal's principle not proved")
    
a=input("Enter a fraction:")
b=input("Enter another fraction:")
n,d=[int(i) for i in a.split("/")]
n1,d1=[int(i) for i in b.split("/")]
prove_pascal(n,d,n1,d1)
