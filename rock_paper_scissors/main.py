from random import randint


def user_result(options):
    for index, option in enumerate(options):
        print(f'{index} = {option}')
    user = int(input("What do you choose? "))
    return user


def computer_result(content):
    computer_choose = randint(0, len(content) - 1)
    return computer_choose


def checking_results(content, player, computer):
    if player == computer:
        return "It's tie!"
    elif (player == 0 and computer == len(content) - 1) or (
            player > computer and not (player == len(content) - 1 and computer == 0)):
        return "Player WON!!"
    return "Player LOSE(("


def play(content):
    print("""
    Welcome to the famous game 'Rock, paper and scissors'
    Pick your weapon
    """)
    user_results=user_result(content)
    computer_results=computer_result(content)
    print("Player chose: {}".format(content[user_results]))
    print("Computer chose: {}".format(content[computer_results]))
    result=checking_results(content,user_results,computer_results)
    print(result)
option_list=["Rock","Paper","Scissors"]
y_n=''
while y_n!="n":
    play(option_list)
    print()
    y_n=input("Do you want to play again? y/n ")

