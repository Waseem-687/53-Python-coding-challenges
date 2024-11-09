def main():
    print("This program is about print ones digit! :")
def print_ones_digit(num):
    """Prints the ones digit of the given integer."""
    ones_digit = num % 10  # Get the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    """Main function to get user input and call print_ones_digit."""
    # Prompt the user for a number
    user_input = input("Enter a number: ")
    
    try:
        # Convert the input to an integer
        number = int(user_input)
        
        # Call the print_ones_digit function with the user's number
        print_ones_digit(number)
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid integer.")

# Run the main function
main()

if __name__ == '__main__':
    main()