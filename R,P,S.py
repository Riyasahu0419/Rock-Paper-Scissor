import random

print("*🙏 WELCOME TO GAME 🙏*")
print("---------------------------------")
options = {1: "Rock 👊", 2: "Paper ✋", 3: "Scissor ✌"}
print("---------------------------------")
print(""" The Winning Rules of this game are:
Rock 👊 vs Paper ✋ --> Paper wins ✋
Rock 👊 vs Scissor ✌ --> Rock wins 👊
Paper ✋ vs Scissors ✌ --> Scissor wins ✌""")
print("---------------------------------")
print("** GET READY TO PLAY **\n")
print("---------------------------------")

user = 0
computer = 0
tie = 0
playagain = "Yes"

while playagain.lower() == "yes":
    user_ch = int(input("Choose your option (1-Rock, 2-Paper, 3-Scissor): "))

    while user_ch not in [1, 2, 3]:
        print("Invalid option. Please choose among 1, 2, and 3 only.")
        user_ch = int(
            input("Choose your option (1-Rock, 2-Paper, 3-Scissor): "))

    print("Your choice is", options[user_ch])

    comp_ch = random.randint(1, 3)
    print("The choice of computer is", options[comp_ch])

    if user_ch == comp_ch:
        print("IT'S A DRAW/TIE 👔🙌")
        tie += 1
    elif ((user_ch == 1 and comp_ch == 2) or (user_ch == 2 and comp_ch == 3) or (user_ch == 3 and comp_ch == 1)):
        print("ohh No 😰 The WINNER IS YOUR COMPUTER 🎉")
        computer += 1
    else:
        print("CONGRATS USER 💁🎉, YOU WON THIS GAME 👑")
        user += 1

    print("---------------------------------")
    playagain = input("Do you want to play again? (Yes/No): ")

print("\nUser score is", user)
print("Computer score is", computer)
print("Tie score is", tie)
if user == computer:
    print("** OVERALL It's a TIE 🙌**")
elif user > computer:
    print("OVERALL the USER wins 🎉✨")
else:
    print("Finally COMPUTER wins 🎉🥳")
