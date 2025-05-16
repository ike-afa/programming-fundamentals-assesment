import random

class Game:
    def __init__(self, word_file):
        file = open(word_file,'r')
        words = file.read().lower().splitlines()
        file.close()
        index = random.randint(0, len(words) - 1)
        self.word = words[index]
        self.bad_guesses = []
        self.attempt_letters = ['_' for c in self.word]
    
    def play(self):
        guesses=[]
        while not self.game_over():
            guess = ""
            while len(guess)!=1 or guess<'a' or guess>'z':
                guess = input("whats your guess? ")
            guesses.append(guess)
            print(guesses)
            
    
    def attempt(self):
        return "".join(self.attempt_letters)
    
    def game_over(self):
        return len(self.bad_guesses) >= 8 or self.attempt() == self.word

def main():
    
    game = Game('names.txt')
    
    game.play()
    
if __name__ == '__main__':
    main()



