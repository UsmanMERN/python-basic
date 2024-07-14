entered_year = input("Enter the year you wants to check \n")

year_to_int = int(entered_year)

if (year_to_int % 4 == 0 and year_to_int % 100 != 0) or (year_to_int % 400 == 0):
    print("This is LEAP YEAR", year_to_int)
else:
    print(year_to_int, "NOT a leap year")
