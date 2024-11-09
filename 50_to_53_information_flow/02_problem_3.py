def main():
    print("This program is about mplement the following function which takes in 3 integers as parameters! :)")
def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high  # Check if n is within the inclusive range from low to high

def main():
    """Main function to get user input and call in_range."""
    # Prompt the user for input values
    try:
        n = int(input("Enter the number to check (n): "))
        low = int(input("Enter the lower bound (low): "))
        high = int(input("Enter the upper bound (high): "))

        # Check if high is greater than low
        if high <= low:
            print("The upper bound (high) must be greater than the lower bound (low).")
            return

        # Call in_range and print the result
        if in_range(n, low, high):
            print(f"{n} is in the range between {low} and {high}.")
        else:
            print(f"{n} is not in the range between {low} and {high}.")

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter valid integers for n, low, and high.")

# Run the main function
main()
