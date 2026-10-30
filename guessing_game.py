class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None
    
    def guess(self, user_guess):
        self.last_guess = user_guess
        if user_guess > self.answer:
            return "high"
        if user_guess == self.answer:
            return "correct"
        if user_guess < self.answer:
            return "low"
    
    def solved(self):
        if self.answer == self.last_guess:
            return True
        else:
            return False
        
game = GuessingGame(10)
print(game.solved())
print(game.guess(5))
print(game.solved())
