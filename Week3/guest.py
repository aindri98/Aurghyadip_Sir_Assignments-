cost=0
while True:
    age=input("Enter the age(Enter a blank line to stop:")
    if (age==""):
        print("No more guests")
        break
    else:
        age=int(age)
        if age<=2:
            cost +=0
        elif 3<=age<=12:
            cost +=14.0
        elif age>=65:
            cost +=18.0
        else:
            cost +=23.0
print(f"The total cost:""{:.2f}".format(cost))
             
        
        
        
    