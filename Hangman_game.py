# This is a prototype of Hangman Game
# Computer will select a random name from the list and user will have 6 lives to guess that name.
# After each wrong selection of word player will lose a life.

# Import created list of name from hangman_words
from Hangman_words import word_list

# Import logo of the game from the hangman design file
from Hangman_design import logo
print(logo)
print("Welcome in Hangman Game")

# Import random library to select word randomly from the list
import random

# Let computer to chose word from the list
chosen_word = random.choice(word_list)
#print(f"Computer chosen word: {chosen_word}")
length_of_word = len(chosen_word)

# Create a list of underscore to display number of letters to player
blank_display = []
for i in range(length_of_word):
    blank_display.append("_")
print(f"Chosen word is : {' '.join(blank_display)}")

# Create a variable for counting lives
lives = 6

# We have to ask player to enter his letter either he has lives or no letter remains
end_of_the_game = False
while not end_of_the_game:
    # Ask player to enter his guessed letter
    guess = input("\nPlease enter your guessed letter: ")
    if len(guess) > 1:
        print("Invalid Input")
    else:
        if guess in blank_display:
            print(f"You have already guessed the letter '{guess}'")
        # Create a loop to check guessed letter with each word of chosen word
        for number in range(length_of_word):
            word = chosen_word[number]
            if word == guess:
                blank_display[number] = guess

        # Lose a life if player guessed the wrong letter
        if guess not in chosen_word:
            lives -= 1
            print(f"Your guessed letter '{guess}' is wrong and you lose a live.")
        print(f"\nYou're chosen word is : {' '.join(blank_display)}")

        # Track playe won the game or not
        if "_" not in blank_display:
            end_of_the_game = True
            print("You won the game")
        # When player will lose the game.
        if lives == 0:
            end_of_the_game = True
            print("You're out of your lives. You loss the game.")
            print(f"The right answer was: {chosen_word}")
        # Print hangman picture and import image from hangman design
        from Hangman_design import stages
        print(stages[lives])