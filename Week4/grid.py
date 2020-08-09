num = eval(input("Enter the start number: "))
x = 0
if -6<num<93:
    for i in range(num,num+42):
        print("{:2}".format(i),end=" ")
        x +=1
        if x == 7:
            x = 0
            print()