import random
from hangman_words import word_list

chosen_word=random.choice(word_list)
display=[]
lives=6

from hangman_art import logo
print(logo)

#testing code
#print(f"The solution is {chosen_word}")

for n in chosen_word :
  display.append("_")  

end_of_game = False
while not end_of_game:
    guess=input("Guess a letter ").lower()
    
    #If the user has entered a letter they've already guessed, printing the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}")
    
    #Check guessed letter
    for i in range(len(chosen_word)) :                
      letter=chosen_word[i]
      if letter == guess:
        display[i]=letter
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")                                   

    #Check if user is wrong.
    if guess not in chosen_word :
      # If the letter is not in the chosen_word, printing out the letter and let them know it's not in the word.
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      
      lives -= 1 
      if lives==0 :
        end_of_game = True
        print("You lose the game.")

    #Check if user has got all letters.
    if "_" not in display :
      end_of_game = True
      print("Congratulations! You won the game.")

    from hangman_art import stages
    print(stages[lives])




