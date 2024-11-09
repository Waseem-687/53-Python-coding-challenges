def main():
    print("function that function count_even! :")
def populate_list():
    """Prompts the user to enter integers until they press enter to stop."""
    lst = []  # Initialize an empty list to store the numbers

    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        # Check if the user pressed enter without typing anything
        if user_input == "":
            break  # Exit the loop if input is empty
        
        try:
            # Try to convert the input to an integer and add it to the list
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")  # Handle invalid input (non-integer)

    return lst

def count_even(lst):
    """Counts the even numbers in a list and prints the count."""
    even_count = 0  # Initialize counter for even numbers

    for number in lst:
        if number % 2 == 0:  # Check if the number is even
            even_count += 1  # Increment the counter if the number is even

    print(f"Number of even numbers: {even_count}")  # Print the total count of even numbers

def main():
    """Main function to execute the program."""
    # Step 1: Populate the list with user input
    numbers = populate_list()
    
    # Step 2: Count and print the even numbers in the list
    count_even(numbers)

# Run the main function
main()


# Python file to call the main() function.
if __name__ == '__main__':
    main()