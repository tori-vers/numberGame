"""guess a secret 3 digit number based on clues 
offers the hint 'Close!' when guess has a correct digit in the wrong place
Closer!' when guess has correct digit in correct place
None' if no correct digits
User has {} tries """

import random

#def for main, generating number, giving clues

NUM_DIGITS = 2
MAX_GUESSES = 10

def main():
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues: ")
    print("When I say:      That means:")
    print("Close            One Digit is correct but in the wrong position")
    print("Closer           One Digit is correct and in the right position")
    print("None             No Digit is correct")

    
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.\nYou have {} guesses to get it.".format(MAX_GUESSES))
        numGuesses = 1
        
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess # {}: ".format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You have run out of guesses.")
                print("The answer was {}".format(secretNum))
                
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
        
    
    
def getSecretNum():
    '''returns a string made up of NUM_DIGITS unique random digits'''
    
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
        
        
def getClues(guess, secretNum):
    '''returns a string with pico, fermi, or bagel as clues'''
    
    if guess == secretNum:
        return "You got it!!"
        
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #correct digit in correct place
            clues.append('Close')
        elif guess[i] in secretNum:
            #correct digit in incorrect place
            clues.append('Closer')
    if len(clues) == 0:
        return 'None'
    
    else:
        #sorts clues into alphabetical order so og order doesn't give info away
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()