import random

USER_SCORE = 0
SERVER_SCORE = 0


def rps():
    user_input = input("Rock, paper, or scissors? ").lower()
    server_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYour input was: {user_input}, the computer's was: {server_choice}\n")

    if user_input == server_choice:
        print("Tie.")
    elif user_input == "rock":
        if server_choice == "scissors":
            print("You win!")
            global USER_SCORE
            USER_SCORE += 1
        else:
            print("Computer wins.")
            global SERVER_SCORE
            SERVER_SCORE += 1
    elif user_input == "paper":
        if server_choice == "rock":
            print("You win!")
            USER_SCORE += 1
        else:
            print("Computer wins.")
            SERVER_SCORE += 1
    elif user_input == "scissors":
        if server_choice == "paper":
            print("You win!")
            USER_SCORE += 1
        else:
            print("Computer wins.")
            SERVER_SCORE += 1
    print(f"Score: you {USER_SCORE}, computer: {SERVER_SCORE}\n")


while USER_SCORE < 5 and SERVER_SCORE < 5:
    rps()

print("You won best out of 5!") if USER_SCORE >= 5 else print("Computer won best out of 5!")
