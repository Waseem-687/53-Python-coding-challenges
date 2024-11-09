def main():
    print("the double(num) function to return the result of multiplying num by 2! :)")
def double(num):
    """Returns the result of multiplying the input number by 2."""
    return num * 2

def main():
    """Main function to get user input, call double, and print the result."""
    # Ask the user to enter a number
    user_input = input("Enter a number: ")
    
    try:
        # Convert the input to a float for flexibility with both integers and decimals
        number = float(user_input)
        
        # Call the double function with the user's number
        result = double(number)
        
        # Print the result of doubling the number
        print(f"Double that is {result}")
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Please enter a valid number.")

# Run the main function
main()
