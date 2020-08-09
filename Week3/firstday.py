import math 
year_1 = int(input("Enter the first year:\n"))
year_2 = int(input("Enter the second year:\n"))

for year in range(year_1,year_2+1):
    n = year - 1
    m = 4
    m_1 = 100
    m_2 = 400
    m_3 = 7
    
    R_1 = 5 * (n % m)
    R_2 = 4 * (n % m_1)
    R_3 = 6 * (n % m_2)

    n_4 = 1 + R_1 + R_2 + R_3
    
    R_4 = n_4 % m_3
    day = R_4
    if day == 0:
        print("The 1st of January",year,"falls on a Sunday.")
    if day == 1:
        print("The 1st of January",year,"falls on a Monday.")
    if day == 2:
        print("The 1st of January",year,"falls on a Tuesday.")
    if day == 3:
        print("The 1st of January",year,"falls on a Wednesday.")
    if day == 4:
        print("The 1st of January",year,"falls on a Thursday.")
    if day == 5:
        print("The 1st of January",year,"falls on a Friday.")
    if day == 6:
        print("The 1st of January",year,"falls on a Saturday.")