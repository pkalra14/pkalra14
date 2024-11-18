# Write the program to take the 2 user input
# then sum the number
#mul -> *
#div -> /

#logic Building
# Step 1
#I/P -> num1, num2 -> int or float
#O/P -> sum - int, sub-> int, div -> float

num1 = int(input("Enter the num 1"))
num2 = int(input("Enter the num 2"))

#num1 = int(num1)
#num2 = int(num2)

print((type(num1)))
print((type(num2)))


# Step 2 | Rough Logic
# sum  =, -, /, *


#Step 3

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1/num2


print("Sum is :", sum)
print("Sub is :", sub)
print("Mul is :", mul)
print("Div is :", div)

