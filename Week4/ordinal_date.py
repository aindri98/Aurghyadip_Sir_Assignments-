arr=[int(31),int(28),int(31),int(30),int(31),int(30),int(31),int(31),int(30),int(31),int(30),int(31)]
m=0
def leap_year(year):
    return (bool(year %4 ==0 and (year % 100 != 0 or year % 400 == 0)))    
def OrdinalDate(day,month,year):
    if(month-1==1):               
        if(leap_year(year)):
            arr[month-1]+1
        else:
            arr[month-1]
    else:    
        arr[month-1]
    for i in range(0,month-1):
        day=day+arr[i]
    return day


if __name__ == '__main__':
    day=int(input("Enter the day:"))
    month=int(input("Enter the month(1-12)"))
    year=int(input("Enter year:"))
    output=OrdinalDate(day,month,year)
    print(f"Ordinal date:{output}")

        
    
    
    