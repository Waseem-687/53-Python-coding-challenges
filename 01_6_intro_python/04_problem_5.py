def main():
    print("This program is written to calculate and print the perimeter of the triangle! :)")

# Prompt the user for the lengths of each side
side1 : float = float(input("What is the length of side 1? "))
side2 : float = float(input("What is the length of side 2? "))
side3 : float = float(input("What is the length of side 3? "))


# Display the result
print("The perimeter of the triangle is " + str(side1 + side2 + side3))
      
if __name__ == '__main__':
    main()