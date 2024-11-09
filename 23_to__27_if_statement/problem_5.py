def main():
    print("This program is about random numbers! :")
import random

def print_random_numbers():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):
        value = random.randint(1, 100)
        print(value, end=" ")

# Run the function
print_random_numbers()

if __name__ == '__main__':
    main()
