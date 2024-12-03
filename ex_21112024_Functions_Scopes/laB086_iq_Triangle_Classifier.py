# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


def classify_traingle(a,b, c):
    if a > 0 or b > 0 or c > 0:
        if a + b > c and a + c > b and b + c > c:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or c == a:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not a valid length")

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

result = classify_traingle(side1, side2, side3)
print(f"The triangle is classified as: {result}")