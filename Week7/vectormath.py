a = input("Enter vector A:\n")
b = input("Enter vector B:\n")
a = (a.split())
b = b.split()

x=""
r=0
c=int(a[0])+int(b[0])
d=int(a[1])+int(b[1])
e=int(a[2])+int(b[2])   
x=x+"["+str(c)+", "+str(d)+", "+str(e)+"]"

r=int(a[0])*int(b[0])+int(a[1])*int(b[1])+int(a[2])*int(b[2])

from math import sqrt
v = sqrt(int(a[0])**2 + int(a[1])**2 +int(a[2])**2 )
z = sqrt(int(b[0])**2 + int(b[1])**2 +int(b[2])**2 )

if v == 0:
    v = "0.00"
elif v != 0:
    v = round(v,2)
if z == 0:
    z = "0.00" 
elif z != 0:
    z = round(z,2)

print("A+B = ",x, sep = '')
print("A.B =",r)
print("|A| =",v)
print("|B| =",z)