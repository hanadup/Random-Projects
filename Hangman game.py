import random

import pictures

import extendedwordlist

import os
print(pictures.logo)
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(extendedwordlist.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    os.system('cls')

    if guess in display:
        print("You have already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("Your guessed letter is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(pictures.stages[lives])
