# Match Statement -> # Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block


# Write a program to ask the user which browser he want to run automation.

browser_name = input("Enter the browser name \n")
match browser_name:
    case "firefox" :
        print("Starting Firefox!!!")
    case "chrome" :
        print("Execute the Chrome Code")
    case "Safari" :
        print("Execute the Safari Code")
    case "edge" :
        print("Execute the edge")
    case _: #default
        print("Browser not found")

