base_fare=4.00
variable_fare=0.25
def taxifare_calc(dis):
    total_cost= base_fare + (((dis*1000)/140)*variable_fare)
    return total_cost
def main():
    dis=taxifare_calc(int(input("Enter the distance(in kms)")))
    print("The total fare :{:.2f}".format(dis))
    
main()
    

