MAX_TERM_VALUE : int = 10000

def main():
    print("This Program is about Fibonacci sequence up to a maximum value! :")
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# Python file to call the main() function.
if __name__ == '__main__':
    main()