def main():
    print("This program is written for to solve age-related riddle)")
# Given ages and relationships
anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age

# Printing each person's name and age in the specified format
print(f"Anton is " + str(anton_age))
print(f"Beth is " + str(beth_age))
print(f"Chen is " + str(chen_age))
print(f"Drew is " + str(drew_age))
print(f"Ethan is " + str(ethan_age))

# Python file to call the main() function.
if __name__ == '__main__':
    main()