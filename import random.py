import random

def hangman():
    
    words = ['python', 'lingesh', 'programming', 'data', 'model']
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_completion = ['_'] * len(word)

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while incorrect_guesses < max_incorrect_guesses and '_' in word_completion:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_completion[index] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print(" ".join(word_completion))

    if '_' not in word_completion:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
