import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
lives = 6

print(logo)
chosen_word = random.choice(word_list)
# For test :
# print(f'The solution is {chosen_word}.')

display_lst = []
letter_g_lst = []
for _ in range(len(chosen_word)):
    display_lst.append("_")

while end_of_game is False:
    letter_guess = input("Guess a letter: ").lower()

    if letter_guess in display_lst:
        print(f"You already guessed {letter_guess}, please use a different letter")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            letter_g_lst.append(letter_guess)
            if letter == letter_guess:
                display_lst[position] = letter

        if letter_guess not in chosen_word:
            print(f"You guessed {letter_guess},that's not in the word! You lose a life!")
            print(stages[lives])
            lives -= 1

    # revel word
    print(f"{' '.join(display_lst)}")

    if "_" not in display_lst:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print(stages[lives])
        print("You lost! ")
