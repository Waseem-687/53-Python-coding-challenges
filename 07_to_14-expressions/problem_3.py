def main():
    print("This program that converts feet into inches! :")
# Constant for inches per foot
INCHES_PER_FOOT = 12

# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Main program
try:
    # Get user input for feet
    feet = float(input("Enter the measurement in feet: "))
    
    # Convert to inches
    inches = feet_to_inches(feet)
    
    # Determine correct singular or plural forms
    feet_unit = "foot" if feet == 1 else "feet"
    inches_unit = "inch" if inches == 1 else "inches"
    
    # Display the result
    print(f"{feet} {feet_unit} is equal to {inches} {inches_unit}.")
    
except ValueError:
    print("Please enter a valid number for feet.")

if __name__ == '__main__':
    main()