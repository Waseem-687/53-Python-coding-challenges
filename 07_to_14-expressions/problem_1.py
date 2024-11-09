def main():
    print("This Expression function is for rolling two dice! :)")
import random
def roll_dice():
    dice1 = random.randint(1, 6)  # Local variable for the first dice
    dice2 = random.randint(1, 6)  # Local variable for the second dice
    print(f"Dice 1: {dice1}, Dice 2: {dice2}")

# Main code to roll dice three times
for i in range(3):
    print(f"Roll {i+1}:")
    roll_dice()

# Python file to call the main() function.
if __name__ == '__main__':
    main()