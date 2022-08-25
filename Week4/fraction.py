m=0
def gcd(n,d):
    if n>d:
        m=n
    else:
        m=d
    while n%m!=0 or d%m!=0:
        m-=1
    return m
def reducefraction(n,d):
    result=gcd(n,d)
    return(n/result,d/result)

if __name__ =='__main__':
    n=int(input("Enter the Numerator:"))
    d=int(input("Enter the denominator:"))
    n1,d1=reducefraction(n,d)
    result="/".join([str(n1),str(d1)])
    print(f"Reduced Fraction:{result}")