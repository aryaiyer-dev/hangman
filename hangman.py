# This is the Hangman python script
#Members: Arya Iyer, Ananya Baphna, Elaine Wang, Diana Naida, Rishita Mudradi
import random


def initialize_word_bank():
    #Return a list of English words between 4 and 12 letters.
    words_set = ("bird","python","cool","zebra","research","institution","purple","happy")
    return [word for word in words_set if 4 <= len(word) <= 12]


alphabet = set("abcdefghijklmnopqrstuvwxyz")


def play_single_game(word_list):
    #Play one round of Hangman.

    secret_word = random.choice(word_list)
    guessed_letters = []
    lives = 6

    # Create the blank display
    display = ["_"] * len(secret_word)
    word_length = len(secret_word)

    print("Let's play Hangman!")
    print(" ".join(display))

    while lives > 0 and "_" in display:

        guess = input("Guess a letter: ").strip().lower()

        # Check for exactly one character
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        # Check that it's a letter
        if guess not in alphabet:
            print("Please enter a valid letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")

            for i in range(word_length):
                if secret_word[i] == guess:
                    display[i] = guess

        else:
            lives -= 1
            print(f"Wrong! You have {lives} lives left.")

        print("Word:", " ".join(display))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

    if "_" not in display:
        print("Congratulations! You win!")
        print(f"The word was: {secret_word}")
    else:
        print("Game over!")
        print(f"The word was: {secret_word}")


def main():
    """Main game loop."""

    word_list = initialize_word_bank()

    while True:
        play_single_game(word_list)

        response = input("Play again? (y/n): ").strip().lower()

        if response == "y":
            print("Starting a new game...")
        elif response == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Exiting game.")
            break


if __name__ == "__main__":
    main()
