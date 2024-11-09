def main():
    print("This function is used for Read mass from user input!: ")
# Speed of light in meters per second
C = 299792458  

while True:
    try:
        # Read mass from user input
        mass = float(input("Enter kilos of mass (or type 'exit' to quit): "))
        
        # Calculate energy using the formula E = m * c^2
        energy = mass * C**2
        
        # Display the results
        print("\ne = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")

    except ValueError:
        print("Please enter a valid number for mass or type 'exit' to quit.")

# Python file to call the main() function.
if __name__ == '__main__':
    main()