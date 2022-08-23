sum,c=0,0
avg=0
while True:
    n=int(input("Enter the number:"))
    if(n==0):
        if(c==0):
            print("You can't end before you begin")
            continue
        else:
            print("End of the numbers")
            break
    else:
        sum +=n
        c +=1
        
    
avg=sum/c
print(f"average:{avg}")
