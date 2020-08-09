num = eval(input("Enter a number: "))

if -6<num<2:
    for i in range(num,num+41,7):
        print("{:>2}".format(i))