m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
if n>m:
    d=n
else:
    d=m
while n%d!=0 or m%d!=0:
    d -=1
print(f"the greatest common divisor:{d}")
