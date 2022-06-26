import random
class Validation:
    def inList(self, message, accepted):
        string = input(message)
        while string.upper() not in accepted:
            valid = "/".join(accepted)
            string = input(f"Please enter a valid value [{valid}]")
        return string
    
    def isNumber(self, message):
        try:
            string = round(float(input(message)), 2)
            return string
        except:
            return round(self.isNumber(), 2)
        
class Game:
    playerScore = 300
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    currentCard = random.choice(cards)
    nextCard = random.choice(cards)
    ifScore = 100
    ifLoses = 75
    gameOver = False
    def __init__(self, playerName):
        self.playerName = playerName
    
    def round(self):
        inpt = Validation()
        playAgain = "Y"
        while playAgain.upper() == "Y":
            cc = f" {str(self.currentCard).zfill(2)} "
            nc = f" {str(self.nextCard).zfill(2)} "
            print(f"""
              Current Card:
                  ----
                 |    |
                 |{cc}|
                 |    |
                  ----
""")
            guess = inpt.inList("The next card is Higher or Lower? [H/L]: ", ["H", "L"])
            if(guess.upper() == "H"):
                if(self.currentCard < self.nextCard):
                    correct = True
                else:
                    correct = False
            else:
                if(self.currentCard > self.nextCard):
                    correct = True
                else:
                    correct = False
            print(f"""
            Current Card:    The next card was:
                 ----               ----
                |    |             |    |
                |{cc}|             |{nc}|
                |    |             |    |
                 ----               ----
""")
            if(correct):
                self.playerScore = self.playerScore + self.ifScore
            else:
                self.playerScore = self.playerScore - self.ifLoses
                
            print(f"Your Score is: {self.playerScore}")
                
            if(self.playerScore > 0):
                playAgain = inpt.inList("Play again? [Y/N]: ", ["Y", "N"])
                self.nextCard = random.choice(self.cards)
                self.currentCard = random.choice(self.cards)
            else:
                playAgain = "N"
        print(f"""      
 ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
|    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    |
| 01 | | 02 | | 03 | | 04 | | 05 | | 06 | | 07 | | 08 | | 09 | | 10 | | 12 | | 13 |
|    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    |
 ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
Oops, Game Over.
Your score was: {self.playerScore}
""")
        
def menu():
    inpt = Validation()
    print("Welcome to Hilo Game!")
    selected = inpt.isNumber("Game Menu:\n1. Play\n2. Instructions\n3. Quit\nSelect:")
    if selected == 1:
        play()
    if selected == 2:
        print("""
>> The player starts the game with 300 points.
>> Individual cards are represented as a number from 1 to 13.
>> The player guesses if the next one will be higher or lower.
>> The the next card is displayed.
>> The player earns 100 points if they guessed correctly.
>> The player loses 75 points if they guessed incorrectly.
>> If a player reaches 0 points the game is over.
>> If a player has more than 0 points they decide if they want to keep playing.
>> If a player decides not to play again the game is over.
""")
        menu()
    if selected == "3":
        return False
def play():
    pName = input("Please type yout name: ")
    g = Game(pName)
    
    print(f"""      
 ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
|    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    |
| 01 | | 02 | | 03 | | 04 | | 05 | | 06 | | 07 | | 08 | | 09 | | 10 | | 12 | | 13 |
|    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    | |    |
 ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
 Hi {g.playerName}! Welcome to Hilo
""")
    g.round()
    
    
    
    
menu()