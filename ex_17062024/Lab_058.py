# Function
# Block of Code - WHich can executed or resued.
# define
# Call

# Built in Functions
# Which are created by the Python Contributers
result = max(2, 3)


# User Define functions
# They can return something
# They can't return --> non return
# They have parameters
# They don't parameters / arguments
#
# def say_hello():  # No return type and No Parameter / Argument
#     print("Hello")
#
#
# say_hello()
#
#
# def say_hello_arg(name):  # NO return Type and with Argument
#     print("Hello",name)
#
#
# say_hello_arg("aiman")
# say_hello_arg("umme")


def say_hello_arg_default(name="aiman"):  # No return Type
  # Write The Code
     print("Hello", name)

say_hello_arg_default()
say_hello_arg_default("Deeksha")
say_hello_arg_default(name="sachin")


def sum_number_argument_ret(a,b):  #Argument + return type
    return a+b

# result = sum_number_argument_ret(3,4)
# result = sum_number_argument_ret(a=31, b=43)
# result = sum_number_argument_ret(a=90,b=89)
result = sum_number_argument_ret(a=99,b=101)
print(result)

