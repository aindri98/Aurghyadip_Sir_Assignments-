
arr=[int(31),int(28),int(31),int(30),int(31),int(30),int(31),int(31),int(30),int(31),int(30),int(31)]
def leap_year(y):
    return (bool(y %4 ==0 and (y % 100 != 0 or y % 400 == 0)))    
def Number_of_daysCalc(m,y):
            if(m-1==1):               
                if(leap_year(y)):
                        return arr[m-1]+1
            else:    
                return arr[m-1]

if __name__ == '__main__':
    m=int(input("Enter the month:"))
    y=int(input("Enter the year:"))
    n=Number_of_daysCalc(m,y)
    print(f"The number of days in the month {m} is {n}.")