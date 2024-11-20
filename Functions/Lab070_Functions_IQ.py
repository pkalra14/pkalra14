# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
num3 = int(input("Enter the num3"))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 +n3

result = sum_of_three(num1, num2, num3)
print(result)

result2 = sum_of_three()
print(result2)