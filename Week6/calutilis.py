def is_leap_year(year):
     
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def month_name(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "February"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    
        
def days_in_month(month_number, year):
    if month_number == 1:
        return 31
    elif month_number == 3:
        return 31
    elif month_number == 4:
        return 30
    elif month_number == 5:
        return 31
    elif month_number == 6:
        return 30
    elif month_number == 7:
        return 31
    elif month_number == 8:
        return 31
    elif month_number == 9:
        return 30
    elif month_number == 10:
        return 31
    elif month_number == 11:
        return 30
    elif month_number == 12:
        return 31
    """This is for case of February which changes when there is a leap year"""
    if is_leap_year(year) and month_number == 2:
        return 29
    else:
        return 28

def first_day_of_year(year):
    """This algorithm calculates the first day of the year"""
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
    """This if statements are responsible for returning the weekdays that started the year"""
    if day == 0:
        return 0
    if day == 1:
        return 1
    if day == 2:
        return 2
    if day == 3:
        return 3
    if day == 4:
        return 4
    if day == 5:
        return 5
    if day == 6:
        return 6
    
def first_day_of_month(month_number,year):
    import datetime
        
    if month_number == "January":
        month = 1
    elif month_number == "February":
        month = 2
    elif month_number == "March":
        month = 3
    elif month_number == "April":
        month = 4
    elif month_number == "May":
        month = 5
    elif month_number == "June":
        month = 6
    elif month_number == "July":
        month = 7
    elif month_number == "August":
        month = 8
    elif month_number == "September":
        month = 9
    elif month_number == "October":
        month = 10
    elif month_number == "November":
        month = 11
    elif month_number == "December":
        month = 12
        
    date = datetime.date(int(year),int(month_number),1)
    weekday = date.isoweekday()
    
    if weekday == 1:
        return 1
    elif weekday == 2:
        return 2
    elif weekday == 3:
        return 3
    elif weekday == 4:
        return 4
    elif weekday == 5:
        return 5
    elif weekday == 6:
        return 6
    elif weekday == 7:
        return 0
        