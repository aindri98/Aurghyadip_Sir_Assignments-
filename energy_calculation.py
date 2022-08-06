from multiprocessing.managers import ValueProxy


m=int(input("Enter mass: "))
h=int(input("Enter height: "))
v=int(input("Enter velocity: "))
g=9.8
KE=0.5*m*v*v
PE=m*g*h
print(f"kinetic energy={KE}J")
print(f"Potential energy={PE}J")
