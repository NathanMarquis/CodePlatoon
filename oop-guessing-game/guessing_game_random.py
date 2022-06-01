import random

class GuessingGameRandom():
    def __init__(self, range):
        self.range = range
        self.answer = random.randint(1, self.range)
        self.continuePlaying = True
        self.is_solved = False
        self.count = 0
        
    def guess(self):
        self.response = []
        try:
            self.user_guess = int(input("Enter your guess\n"))
        except: 
            print('That is not a number, try again!')   #Exception case if they decide to input something dumb
            self.guess()
        
        while self.continuePlaying:
            self.count += 1
            if self.user_guess > self.answer:
                self.response = ["Unfortunately", "too high"]
            elif self.user_guess < self.answer:
                self.response = ["Unfortunately", "too low"]
            elif self.user_guess == self.answer:
                self.is_solved = True
                self.response = ["Congratulations", "correct"]

            print(f"{self.response[0]} your answer was {self.response[1]}")
            if self.is_solved ==  True:
                player_commitment = input(f'You guessed the correct answer in {self.count} tries.\nWould you like to play again? Y/N\n')
                if player_commitment == "Y" or player_commitment == "y":    #Explicitly put either case! That was it
                    self.answer = random.randint(1, self.range)
                    self.is_solved = False
                    self.count = 0
                else:       #Anything other than 'y' or 'Y' will be an exit. NO MEANS NO!!!
                    self.continuePlaying = False
                    exit()
                    
            self.guess()
          
game = GuessingGameRandom(5) #Change number to be range of random number generator
print(game.guess())
