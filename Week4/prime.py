def isPrime(x):
    c=0
    if(x<1):
        return False
    elif(x==1):
        return True
    else:
        for i in range(2,x):
            if(x%i==0):
                c+=1
                break
        if (c==0):
            return True
        else:
            return False
if __name__ == '__main__':
    x=int(input("Enter the number:"))
    print(isPrime(x))
    if(isPrime(x)):
        print("Prime")
    else:
        print("Not prime")
        
        
    
    
    