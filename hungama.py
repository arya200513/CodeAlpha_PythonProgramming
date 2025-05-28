import random

def hangman():
    words = ["python", "apple", "hangman", "challenge", "program"]
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect and word_letters:
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word:", ' '.join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print("Wrong guess!")

        print()

    if not word_letters:
        print(f"Congratulations! You guessed the word '{word}' correctly.")
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()


