from  days import Number_of_daysCalc
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