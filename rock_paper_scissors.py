import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'The computer also chose '+ computer + '. It is a tie'
    
    if win(user, computer):
        return 'The computer chose ' + computer + "\n You won"
    
    return 'The computer chose ' + computer + 'You lost'


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

print(play())

    
