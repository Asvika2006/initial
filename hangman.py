import random

def hangman():
    print("Welcome to Hangman!")
    word_list = ["python", "hangman", "programming", "developer", "artificial"]
    secret_word = random.choice(word_list)
    guessed_word = ["_"] * len(secret_word)
    attempts = 6
    guessed_letters = []

    print("\nGuess the word: " + " ".join(guessed_word))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print("\nCurrent word: " + " ".join(guessed_word))

        if "_" not in guessed_word:
            print("\n🎉 Congratulations! You guessed the word:", secret_word)
            break

    if "_" in guessed_word:
        print("\n😢 Out of attempts! The word was:", secret_word)

if __name__ == "__main__":
    hangman()
