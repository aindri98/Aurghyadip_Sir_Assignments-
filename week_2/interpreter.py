def calculator(x,y,z):
    x=int(x)
    z=int(z)
    if y=="+":
        result=float(x+z)
        print("{:.1f}".format(result))
    elif y=="-":
        result=float(x-z)
        print("{:.1f}".format(result))
    elif y=="*":
        result=float(x*z)
        print("{:.1f}".format(result))
    elif y=="/":
        if(z!=0):
            result=float(x/z)
            print("{:.1f}".format(result))
        else:
            print("can't divide by zero")        
x,y,z=input("Enter the values and operator:").split()
calculator(x,y,z)
