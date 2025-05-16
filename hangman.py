import random

def main():
    file = open('names.txt','r')
    words = file.read().splitlines()
    file.close()

    index = random.randint(0, len(words) - 1)
    word = words[index]

    print(word)

    guesses=[]
    guess = input("whats your guess? ")
    while len(guess)!=1 or guess<'a' or guess>'z':
        guess = input("whats your guess? ")
    guesses.append(guess)
    print(guesses)

if __name__ == '__main__':
    main()



