c=0
arr=[]
while True:
    n=int(input("Enter the number:"))
    if(n==0):
        if(c==0):
            continue
        else:
            break
    else:
        c+=1
        arr.append(n)
arr.sort()
[print(i) for i in arr]

        