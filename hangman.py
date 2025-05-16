import random

class Game:
    def __init__(self, word_file):
        file = open(word_file,'r')
        words = file.read().lower().splitlines()
        file.close()
        index = random.randint(0, len(words) - 1)
        self.word = words[index]

def main():
    
    game = Game('names.txt')
    

    print(game.word)
    return
        

    guesses=[]
    guess = input("whats your guess? ")
    while len(guess)!=1 or guess<'a' or guess>'z':
        guess = input("whats your guess? ")
    guesses.append(guess)
    print(guesses)

if __name__ == '__main__':
    main()



