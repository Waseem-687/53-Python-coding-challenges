def main():
    print(" This program is used for noun adjective verb! :)")
# Define the start of the sentence
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

# Prompt the user for input
adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

# Construct and print the final sentence
print(f"{SENTENCE_START} {adjective} {noun} {verb}!")



# Python file to call the main() function.
if __name__ == '__main__':
    main()