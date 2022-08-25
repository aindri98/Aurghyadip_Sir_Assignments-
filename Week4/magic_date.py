arr=[int(31),int(28),int(31),int(30),int(31),int(30),int(31),int(31),int(30),int(31),int(30),int(31)]
def leap_year(y):
    return (bool(y %4 ==0 and (y % 100 != 0 or y % 400 == 0)))    
def Number_of_daysCalc(m,y):
            if(m-1==1):               
                if(leap_year(y)):
                    return arr[m-1]+1
                else:
                    return arr[m-1]
            else:    
                return arr[m-1]

def magicDate_check(k,m,y):
    return(bool((k*m)==(y%100)))

if __name__ == '__main__':
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    for y in range(1901,2001):
        print(f"year:{y}")
        for m in range(1,13):
            for k in range(1,Number_of_daysCalc(m,y) + 1):
                if(magicDate_check(k,m,y)):
                    print(f"{months[m-1]} {k}")