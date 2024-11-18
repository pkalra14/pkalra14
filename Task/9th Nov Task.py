# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("First Number is"))
num2 = int(input("Second Number is"))

quotient = int(num1 // num2) # using floor division to get the quotient
remainder = int(num1 % num2) # using the
print("quotient is : ", quotient)
print("remainder is : ", remainder)


# Task 2 for the Today
# Take a 3 input from the user
# perform the sub, sub, mul and div

num1 = int(input("First Number is"))
num2 = int(input("Second Number is"))
num3 = int(input("Third Number is"))

sum = num1 + num2 + num3
sub = num1 - num2 - num3
mul = num1 * num2 * num3
div = num1/num2

print("sum is", sum)
print("sub is", sub)
print("mul is", mul)
print("div is", div)


