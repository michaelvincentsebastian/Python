import random
    
def randomBot():
    bot = random.randint(1, 3)
    if bot == 1:
        return 'rock'
    elif bot == 2:
        return 'paper'
    else:
        return 'scissors'

def winConditions(player, bot):
    if player == bot:
        return "It's a draw!"
    elif (player == 'scissors' and bot == 'rock') or \
         (player == 'rock' and bot == 'paper') or \
         (player == 'paper' and bot == 'scissors'):
        return 'bot wins'
    else:
        return 'player wins'

troops = ('rock', 'paper', 'scissors')
userInput = input("Enter your Troops: ").lower()
while userInput not in troops:
    userInput = input("Enter again: ").lower()
    
botMove = randomBot()

print("Player chose: "+ userInput)
print("Bot chose: "+ botMove)

result = winConditions(userInput, botMove)
print(result)
