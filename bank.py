def greetings(gtt):
    if(gtt=="hello"):
        output=0
    elif(gtt[0]=="h"):
        output=20
    else:
        output=100
    print(output)
greetings(input("Enter greeting:"))
    