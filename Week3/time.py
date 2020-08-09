hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

if hours in range(0,24) and minutes in range(0,60) and seconds in range(0,60):
  print("Your time is valid.")
else:
  print("Your time is invalid.")