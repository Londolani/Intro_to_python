pi = 0.0
for i in range(1,10000000,4):
  pi+= 4/i
  pi-= 4/(i+2)

print("Approximation of pi:",round(pi,3))
radii = float(input("Enter the radius:\n"))
Area = 3.1416 * radii **2
print("Area:",round(Area,3))