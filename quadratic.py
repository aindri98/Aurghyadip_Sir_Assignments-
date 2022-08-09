import math
def quadratic_root(a,b,c):
    a,b,c=int(a),int(b),int(c)
    d=((b*b)-(4*a*c))
    if(d>0):
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print(f"The roots are {r1} and {r2} and are real and different")
    elif(d==0):
        r1=r2=(-b+math.sqrt(d))/(2*a)
        print(f"The roots are {r1} and {r2} and are equal")
    else:
        print("The roots are imaginary")

a, b, c = input("Enter the values of a, b and c : ").split()
quadratic_root(a,b,c)
 
    