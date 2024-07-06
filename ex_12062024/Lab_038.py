# Conditions and loop
#age >18 --> You are allowed to go to club
#age <18 --> You are not allowed to go to club

# aiman --> goa --> father permission
# aiman --> no goa --> no permission

# If, ELSE
# Syntax
# if condition:
#    code to be executed
# else:
#    code to be executed when condition is false

# Write a program to take a user age and let him know if he can go to the club.

# Take a user input

age = int(input("Enter your Age"))

if age > 18:
    print("Go the the club")
else:
    print("Not allowed")