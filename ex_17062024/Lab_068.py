# A leap year divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if_else statement to make this determination.

year = 2024

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("not leap year")
