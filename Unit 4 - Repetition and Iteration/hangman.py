import random

def display_word(hidden, guessed):
    display = ""
    # iterate through hidden 
    for index in range(len(hidden)):
        letter = hidden[index]
        if letter in guessed:
            display += letter
        else:
            display += "_"
    
    return display

def hangman():
    words = ["alphabet", "placeholder","cellphone","computer","algorithm","microsoft"]
    hidden = random.choice(words)
    
    maxGuesses = 5
    gameover = False
    numguesses = 0
    guessedletters = ""
    while(not gameover):
        print(display_word(hidden, guessedletters))
        guess = input("Choose a letter: ")
        if guess in guessedletters:
            print("Enzo said you already picked that. That's not very smart.")
        elif len(guess)>1:
            print("Enzo said that's not a letter.")
        elif not (guess in hidden):
            print(guess + " is not in the word.")
            numguesses +=1
            guessedletters += guess
            if numguesses == maxGuesses:
                print("You lose!")
                gameover = True
        else:
            guessedletters += guess
            if display_word(hidden,guessedletters) == hidden:
                gameover = True
                print("You win!")
            
            
hangman()        
                
        
            
        
        
    

    
    