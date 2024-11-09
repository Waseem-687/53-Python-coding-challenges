def main():
    print("This program is written for a number from user input and print its square! :")
    # Prompt the user for a number
    number = float(input("Type a number to see its square: "))

    # Calculate the square of the number
    square = number * number

    # Display the result
    print(f"{number} squared is {square}")
if __name__ == '__main__':
    main()

