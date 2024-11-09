MAX_LENGTH = 3

def shorten(lst):
    # Loop until the list is MAX_LENGTH or shorter
    while len(lst) > MAX_LENGTH:
        # Remove the last element and print it
        removed_element = lst.pop()
        print(removed_element)

# Main function to test shorten()
def main():
    print("This program that that give the final and orignal list! :")
    # Test list
    lst = [1, 2, 3, 4, 5,6,7]
    print("Original list:", lst)
    shorten(lst)
    print("Final list:", lst)

# Run the main function
if __name__ == "__main__":
    main()
