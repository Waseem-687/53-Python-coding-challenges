def main():
    print("This program is used for converting fahrenheit into celsius.")
# Prompt the user for input
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

# Display the result
print(f"Temperature: {degrees_fahrenheit}F° = {degrees_celsius:.2f}C°")

# Python file to call the main() function.
if __name__ == '__main__':
    main()