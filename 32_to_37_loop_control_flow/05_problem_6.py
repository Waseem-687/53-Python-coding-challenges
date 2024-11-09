def main():
    print("This program is about to print double the number untill reach 100 or greater! :")

# Ask the user to enter a number
user_input = input("Enter a number: ")

# Convert the input from string to integer
curr_value = int(user_input)

# Print the initial value
print(curr_value, end=" ")  # Print the original number

# Use a while loop to double the current value until it is 100 or greater
while curr_value < 100:
    # Double the current value
    curr_value = curr_value * 2
    
    # Print the current value after doubling
    print(curr_value, end=" ")  # Print the doubled value


# Python file to call the main() function.
if __name__ == '__main__':
    main()