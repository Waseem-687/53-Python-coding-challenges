def main():
    print("This Function to calculate the hypotenuse! :")
import math

# Function to calculate the hypotenuse
def calculate_hypotenuse(side_a, side_b):
    return math.sqrt(side_a**2 + side_b**2)

# Main program
try:
    # Read the lengths of the two perpendicular sides
    side_a = float(input("Enter the length of AB: "))
    side_b = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    
    # Display the result
    print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    
except ValueError:
    print("Please enter valid numerical values for the lengths of AB and AC.")


if __name__ == '__main__':
    main()