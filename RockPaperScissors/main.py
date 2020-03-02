import random


def correct(word):
    if word.lower() == 'yes' or word.lower() == 'y':
        word = 'yes'
    elif word.lower() == 'no' or word.lower() == 'n':
        word = 'no'
    elif word.lower() == 'rock' or word.lower() == 'r':
        word = 'rock'
    elif word.lower() == 'paper' or word.lower() == 'p':
        word = 'paper'
    elif word.lower() == 'scissors' or word.lower() == 's':
        word = 'scissors'
    return word


def receivePlay():
    while True:
        played = input("Rock, paper or scissors? ")
        played = correct(played)
        if played in ['rock', 'paper', 'scissors']:
            return played


def wins(player, computer):
    if player == 'rock':
        if computer == 'paper':
            return 1
        elif computer == 'scissors':
            return 2
        else:
            return 0
    if player == 'paper':
        if computer == 'scissors':
            return 1
        elif computer == 'rock':
            return 2
        else:
            return 0
    if player == 'scissors':
        if computer == 'rock':
            return 1
        elif computer == 'paper':
            return 2
        else:
            return 0


def playAgain():
    while True:
        ag = input("Play Again?\n")
        answer = correct(ag)
        if answer == 'yes':
            return True
        else:
            return False


pWins = 0
cWins = 0
playing = True
while playing:
    player = receivePlay()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print("Computer plays " + computer)
    winner = wins(player, computer)

    if winner == 2:
        print("You win! ")
        pWins += 1
    elif winner == 1:
        print("You lose! ")
        cWins += 1
    else:
        print("It's a tie! ")

    print("Player wins: " + str(pWins))
    print("Copmuter wins: " + str(cWins))
    playing = playAgain()