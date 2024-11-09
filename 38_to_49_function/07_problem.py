def print_multiple(message, repeats):
    
    """Prints the given message a specified number of times."""
    for _ in range(repeats):
        print(message, end=" ")  # Print the message on the same line with spaces in between

def main():
    """Main function to get user input and call print_multiple."""
    # Prompt the user for a message
    message = input("Please type a message: ")
    
    # Prompt the user for the number of times to repeat the message
    repeat_input = input("Enter a number of times to repeat your message: ")
    
    try:
        # Convert the input to an integer for repeat count
        repeats = int(repeat_input)
        
        # Call the print_multiple function with the user's message and repeat count
        print_multiple(message, repeats)
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid integer for the repeat count.")

# Run the main function
main()
