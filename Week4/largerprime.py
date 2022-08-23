from prime import isPrime
def nextPrime(x):
    while True:
        x+=1
        if(isPrime(x)):
            return x
        else:
             x+1
if __name__ == '__main__':
    n=int(input("Enter the number:"))
    check=nextPrime(n)
    print(f"The  first next prime number:{check}")
    