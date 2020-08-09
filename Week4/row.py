start = eval(input("Enter the start number: "))


if -6<start<93:
    for i in range(start,start+7):
        if i != start+6 :
            print("{:>2}".format(i), end=" ")
        else:
            print("{:>2}".format(i), end="") 