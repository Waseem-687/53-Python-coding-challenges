def add_three_copies(lst, data):
    # Add three copies of 'data' to 'lst'
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    print("This program is about three copies of immutable data types! :")

    # Prompt the user for input
    message = input("Enter a message to copy: ")
    
    # Create an empty list to start with
    my_list = []
    
    print("List before:", my_list)
    
    # Call add_three_copies and observe the changes in the list
    add_three_copies(my_list, message)
    
    print("List after:", my_list)

# Required line to call the main function
if __name__ == '__main__':
    main()

