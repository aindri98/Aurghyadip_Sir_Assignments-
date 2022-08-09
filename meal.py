def convert(time):
    h,m=time.split(":")
    return float(h) + (float(m)/60)
def main():
    time=input("Enter Time:")
    t=convert(time)
    if 7<=t<=8:
        print("Breakfast Time")
    elif 12<=t<=13:
        print("Lunch Time")
    elif 18<=t<=19:
        print("Dinner Time")
main()
