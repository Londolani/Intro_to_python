w1 = eval(input("Enter width 1: "))
h1 = eval(input("Enter height 1: "))  
w2 = eval(input("Enter width 2: "))  
h2 = eval(input("Enter height 2: "))  

price = eval(input("Enter price per metre: "))

total_fence = 2*w1 + 2*w2 + h2 + h1 + h1 - h2 
total_price = total_fence * price 


print("The total fence required = " + str(total_fence) + " metres")
print("The total price = R " + str(total_price))