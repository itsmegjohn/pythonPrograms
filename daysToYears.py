
days = int(input("Enter the number of days:"))
years = days // 365
weeks = (days % 365)//7
remainingDays = days - years*365 - weeks*7

print(years, "Years", weeks, "Weeks", remainingDays, "days")