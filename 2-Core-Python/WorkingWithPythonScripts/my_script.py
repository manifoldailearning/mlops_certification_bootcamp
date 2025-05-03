# Define a global variable
x = 100
print(x)

# Define a function that prints a greeting message
def my_function():
    print("Hello from my_function!")

# Print the name of the current module
print(__name__)

# This block will only execute if the script is run directly (not imported)
if __name__ == "__main__":
    # Call the function
    my_function()
    
    # Get user input for two numbers
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    
    # Calculate and display the sum
    print("The sum of the two numbers is: ")
    print(a + b)



