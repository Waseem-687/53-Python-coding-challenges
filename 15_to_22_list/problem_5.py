def main():
    print("This program is about to get_first_element! :")
    # Prompt the user to enter the number of elements
    num_elements = int(input("Enter the number of elements in the list: "))
    
    # Initialize an empty list
    lst = []
    
    # Collect elements one by one
    for i in range(num_elements):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    
    # Print the first element
    print ("get_first_element(lst)")

# Required line to call main function
if __name__ == "__main__":
    main()

