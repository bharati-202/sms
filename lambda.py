# Lambda function to square a number
square = lambda x: x ** 2

# Normal function to square a number
def square_function(x):
    return x ** 2

# Input from user
num = int(input("Enter a number: "))

# Using lambda function
print("Square using lambda function: ", square(num))

# Using normal function
print("Square using normal function: ", square_function(num))
