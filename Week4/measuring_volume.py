"""
1 tablespoon=3 teaspoons
1 cup=16 tablespoons=48 teaspoons
"""
tsp=0
def ImperialMeasure_Calc(n,x):
    m=""
    if(x=="teaspoon" or x=="teaspoons"):
        tsp=n
    elif(x=="tablespoon" or x=="tablespoons"):
        tsp=n*3
    elif(x=="cup" or x=="cups"):
        tsp=n*48
    cups=int(tsp/48)
    tsp=tsp-(48*cups)
    tbsp=int(tsp/3)
    tsp=tsp-(3*tbsp)
    if(cups>0):
        m=m+str(cups)+"cup"
        if(cups>1):
            m=m+"s"
    if(tbsp>0):  
        m=m+","   
        m=m+str(tbsp)+"tablespoon"
        if(tbsp>1):
            m=m+"s"
    if(tsp>0):
        m=m+","
        m=m+str(tsp)+"teaspoon"
        if(tsp>1):
            m=m+"s"
    if m=="":
        return("zero teaspoon")
    else:
        return m

    
if __name__ == '__main__':
    n=int(input("Enter the number of units:"))
    x=input("Enter the unit of measure(cup(s),tablespoon(s) or teaspoon(s))in lowercase:")
    result=ImperialMeasure_Calc(n,x)
    print(result)