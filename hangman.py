import random

def draw_hangman(incorrect):
    stages = [
     """
        
        
        
        
    =========
    """,
    """
        
    |
    |
    |
    |
    =========
    """,
    """
    +---.
    |
    |
    |
    |
    =========
    """,
    """
    +---.
    |   O
    |
    |
    |
    =========
    """,
    """
    +---.
    |   O
    |   |
    |
    |
    =========
    """,
    """
    +---.
    |   O
    |  /|
    |
    |
    =========
    """,
    """
    +---.
    |   O
    |  /|\\
    |
    |
    =========
    """,
    """
    +---.
    |   O
    |  /|\\
    |  /
    |
    =========
    """,
    """
    +---.
    |   O
    |  /|\\
    |  / \\
    |
    =========
    """
    ]
    print(stages[min(incorrect, len(stages)-1)])
    
class Game:
    def __init__(self, word_file):
        file = open(word_file,'r')
        words = file.read().lower().splitlines()
        file.close()
        index = random.randint(0, len(words) - 1)
        self.word = words[index]
        self.bad_guesses = set()
        self.attempt_letters = ['_' for c in self.word]
        # temporary debugging
        
    
    def play(self):
        while not self.game_over():
            guess = ""
            while len(guess)!=1 or guess<'a' or guess>'z':
                guess = input("whats your guess? ")
            
            # was this a good guess?
            if guess in self.word:
                for i in range(0, len(self.word)):
                    if guess == self.word[i]:
                        self.attempt_letters[i] = guess
            else:
                self.bad_guesses.add(guess)
                
           
            print(self.attempt())
            print(f"bad guesses: {self.bad_guesses}")
            draw_hangman(len(self.bad_guesses))

        
        if self.attempt() == self.word:
            print(f"you won")
        else:
            print(f"too many bad guesses")
    
       
    
       
    
    def attempt(self):
        return "".join(self.attempt_letters)
    
    def game_over(self):
        return len(self.bad_guesses) >= 8 or self.attempt() == self.word

def main():
    
    game = Game('names.txt')
    
    game.play()
    
if __name__ == '__main__':
    main()


 

    


