month = input("Enter the month ('January', ..., 'December'): ")
start = input("Enter the start day ('Monday', ..., 'Sunday'): ")

print(month)
print("Mo Tu We Th Fr Sa Su")
days = {
    "January" : 31,
    "February" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
    }
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for wd in range(7):
    if week[wd] == start:
        wday = wd 
        break
print("   "*wday +" 1"+[" ",""][wday == 6]+ " ".join([" ",""][len(str(i))-1]+str(i) for i in range(2,8-wday)))
cnt = 7-wday
for row in range(5):
    print(" ".join([[" ",""][len(str(i))-1]+str(i)," "][i > days[month]] for i in range(cnt+1+row*7,cnt+1+row*7+7)))