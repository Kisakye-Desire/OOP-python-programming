#function declaration
def is_year_leap(year): 
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:

    # if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)): 
        print(True,  ":", year, "is a leap year")
    else:
        print(False, ":", year, "is not a leap year")

year = int(input("Please Enter a year to check if its a leap year or not: "))

#function call
is_year_leap(year) 