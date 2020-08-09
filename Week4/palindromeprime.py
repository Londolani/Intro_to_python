factors=0
num_1 = eval(input("Enter the start point N:\n"))
num_2 = eval(input("Enter the end point M:\n"))
print("The palindromic primes are:")
for i in range(num_1+1,num_2):
    if str(i)[::-1] == str(i):
        for j in range(1,i+1):
            if i%j==0:
                factors+=1
        if factors==2:
            print(i)
    factors = 0