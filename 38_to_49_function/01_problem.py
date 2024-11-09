def main():
        print("This program about the chaotic_counting! :)")
import random

# Define the likelihood that done() will return True
DONE_LIKELIHOOD = 0.3  # Adjust this to set the likelihood of stopping

def done():
    """Simulates a random chance to stop counting."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Counts from 1 to 10 but stops randomly based on the done() function."""
    for i in range(1, 11):
        if done():               # Check if done() returns True
            return               # Exit the function early if done() is True
        print(i, end=" ")        # Print the current count if not stopping

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()           # Call chaotic_counting() to start counting
    print("\nI'm done.")         # Print "I'm done" after chaotic_counting() finishes

# Run the main function
main()

# Python file to call the main() function.
if __name__ == '__main__':
    main()