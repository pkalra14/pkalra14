# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments

import math

# 1. The can't return -> non return
# No Return Type and No Parameter / Argument - NRNP

def greet():
    print("Hello")

greet()

# 2. # No Return Type and with Argument/ Param

def greet_by_name(name):
    print("Hello", name)

greet_by_name("PK")

# 3. No Return Type and with Default Argument ( # positional argument)

def say_hello_default_arg(name = "Prachi"):
    print("Hello", name.upper())

say_hello_default_arg("Kalra")
say_hello_default_arg()

def multiple_args(name1 = "A", name2 = "B"):
    print("Mul ->", name1, name2)

multiple_args()
multiple_args("Prachi", "Kalra")
multiple_args(name1="Pooja")
multiple_args(name1="Vicky", name2="Kalushal")
multiple_args(name2="Amit")



# 4. Argument + return Type

def sum_of_two(a,b):
    return a + b

result = sum_of_two(4, 56)
print(result)

def sum_of_two_numbers_with_default(num1=100, num2=200):
    return num1 + num2

result = sum_of_two_numbers_with_default(num1=34, num2=34)
print(result)

result = sum_of_two_numbers_with_default()
print(result)
