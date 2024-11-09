def main():
    print("This program is about  to prints out the calls for a spaceship that is about to launch! :")
# Program to print the countdown for a spaceship launch

# Loop to count down from 10 to 1
for i in range(10):                 # The loop will run 10 times (from 0 to 9)
    print(10 - i, end=" ")           # Print the countdown number in reverse order (10, 9, ..., 1)

# Print "Liftoff!" after the countdown
print("Liftoff!")                    # This is printed after the loop ends

# Explanation:
# - range(10) generates numbers from 0 to 9.
# - In each iteration, we calculate 10 - i to get the countdown values.
# - end=" " keeps the output on the same line with a space between numbers.

# Python file to call the main() function.
if __name__ == '__main__':
    main()