import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    getName = input("Enter your name: ")
    choice = int(input("Enter your choice: "))
    print("regrs")
    while choice > 3 or choice < 1:
        print("Invalid choice")
        choice = int(input("Enter a valid choice please: "))
    if choice == 1:
        choiceName = "Rock"
    elif choice == 2:
        choiceName = "Paper"
    elif choice == 3:
        choiceName = "Scissors"
    print(f"{getName} you chose: {choiceName}")
    print("Now its computer turns")

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choiceName = "Rock"
    elif comp_choice == 2:
        comp_choiceName = "Paper"
    else:
        comp_choiceName = "Scissors"
    print("Computer choice is:", comp_choiceName)
    print(choiceName, "vs ", comp_choiceName)
    if choice == comp_choice:
        result = "DRAW"
    elif (comp_choice == 1 and choice == 2) or (comp_choice == 2 and choice == 1):
        result = "Paper"
    elif (comp_choice == 3 and choice == 1) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif (comp_choice == 3 and choice == 2) or (comp_choice == 2 and choice == 3):
        result = "Scissors"

    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choiceName:
        print(f"{getName} you wins")
    else:
        print("<== Computer wins! ==>")
    print(f"{getName} , Do you want to play again?(Y/N)")
    ans = input().lower()
    if ans == "n":
        break


print("Thank you for playing")