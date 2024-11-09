def main():
    try:
        # Ask the user for the two integers
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))
        
        # Calculate the quotient and remainder
        quotient = dividend // divisor
        remainder = dividend % divisor
        
        # Print the results
        print(f"The result of this division is {quotient} with a remainder of {remainder}")
    
    except ValueError:
        print("Please enter valid integer values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero divisor.")

# Required line to call the main() function when the script is run
if __name__ == '__main__':
    main()
