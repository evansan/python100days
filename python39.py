import random
words = ["alex", "math", "apple", "cake", "yeah", "late", "wall", "paws", "kale"]
guessed_letter = []

random_word = random.choice(words)
word_length = (len(random_word ))
attempts = 6

print ( "_ " * word_length)

while attempts > 0:
    guess = input("\nPlease guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only a single letter.")
    elif guess in guessed_letter:
        print("you have gussed this letter")
    elif guess not in random_word:
        print("you gussed the wrong letter")
        attempts -= 1
        print(f"you have {attempts} left")
    elif guess in random_word:
        print("you gussed the right letter")
        guessed_letter.append(guess)


    word_status = " "
    for i in random_word:
        if i in guessed_letter:
            word_status = word_status + i
        else:
            word_status =  word_status + "_"
    
    
    print(word_status)

    if "_" not in word_status:
        print("congrats you won")
    
print(f"Sorry, you have lost. The word was '{random_word}'.")

            


# import random

# def hangman():
#     word_list = ["python", "java", "hangman", "computer", "keyboard", "laptop", "headphones", "mouse"]
#     random_word = random.choice(word_list)
#     guessed_letters = []
#     attempts = 6

#     print("Let's play Hangman!")
#     print("_ " * len(random_word))

#     while attempts > 0:
#         guess = input("\nPlease guess a letter: ").lower()

#         if len(guess) != 1:
#             print("Please enter only a single letter.")
#         elif guess in guessed_letters:
#             print("You have already guessed this letter.")
#         elif guess not in random_word:
#             print("Sorry, this letter is not in the word.")
#             attempts -= 1
#             print(f"You have {attempts} attempts remaining.")
#         else:
#             print("Good job, this letter is in the word!")
#             guessed_letters.append(guess)

#         word_status = ""
#         for letter in random_word:
#             if letter in guessed_letters:
#                 word_status += letter + " "
#             else:
#                 word_status += "_ "
        
#         print(word_status)

#         if "_" not in word_status:
#             print("Congrats, you have won!")
#             return

#     print(f"Sorry, you have lost. The word was '{random_word}'.")

# hangman()
