def ValidTriangle(x,y,z):
    if x==0 or y==0  or z==0 :
        return False
    else:
        return(bool ( z<(x+y) and y<(x+z) and x<(y+z)))
    

if __name__ == '__main__':
    x=int(input("Enter the length:"))
    y=int(input("Enter the length:"))
    z=int(input("Enter the length:"))
    if(ValidTriangle(x,y,z)):
        print("Triangle can be formed")
    else:
        print("Triangle cannot be formed")
        