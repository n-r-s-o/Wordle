import random
import time

times_run = 0

def menu_loop():
    """Loop through menu of various commands based on user input."""

    while True:
        command = input("Start game of Wordle? y/n \n").lower()

        if command == "n":
            exit()
        elif command == "y":
            game()
        elif not command:
            print("Command cannot be empty.")
        else:
            print("Unrecognized command.")

def game():
    """Start playing Wordle."""

    global times_run
    times_run += 1

    if times_run == 1:
        # Print instructions:
        print("\nGame instructions:")
        print("You have 5 rounds to guess a 5-letter word. Each round, you may guess for a new word.")
        print("Example of a correct letter in the right position: a")
        print("Example of a correct letter in the wrong position: (a)")
        print("Good luck!")
        
        time.sleep(1.2)
    
    print()

    word = choose_word()
    word_wip = ["_"] * 5
    facit = []
    facit_letter_counts = {}
    
    for letter in word:
        count = word.count(letter)

        if letter not in facit_letter_counts.keys():
            facit_letter_counts.update({letter: count})

    for letter in word:
        facit.append(letter)

    guesses = []
    round = 1
    game_status = "running"
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    
    wordlist = open("wordlist.txt", "r").readlines()

    while game_status == "running":
        if round > 5:
            game_status = "lost"
            break
        else:
            print(f"- ROUND {round} -")

        if round != 1:
            # Print the word being worked on:
            for letter in word_wip:
                print(letter, end=" ", flush=True)
                time.sleep(0.2)
        else: 
            # Print the word being worked on:
            for letter in word_wip:
                print(letter, end=" ")            

        print()

        word_wip = ["_"] * 5

        print("Letters to guess from: ")
        for letter in alphabet:
            print(letter, end=" ")
        print()

        while True:
            guess = input("Guess a word: ").lower().strip()

            if not guess.isalpha():
                print("Invalid character(s).")
                continue

            elif len(guess) != 5:
                print("Guessed word must be 5 letters.")
                continue
            
            elif guess in guesses:
                print("You've already guessed that word.")
                continue

            elif guess + "\n" not in wordlist:
                print("Word does not exist in the wordlist.")
                continue

            else:
                break

        guessed_letters = []

        for letter in guess:
            guessed_letters.append(letter)
        
        guesses.append(guess)

        correct_but_malplaced = {}
        guess_position = 0

        for guessed_letter in guessed_letters:
            if guessed_letter in facit:
                correct_positions = [index for index, value in enumerate(facit) if value == guessed_letter]

                if guess_position in correct_positions:
                    word_wip[guess_position] = guessed_letter

                if guess_position not in correct_positions:
                    correct_but_malplaced[guessed_letter] = guess_position

                if guessed_letter in alphabet:
                    index = alphabet.index(guessed_letter)
                    alphabet.insert(index, f"[{guessed_letter}]")
                    alphabet.remove(guessed_letter)

            else:
                if guessed_letter in alphabet:
                    alphabet.remove(guessed_letter)     

            guess_position += 1
        
        for letter in correct_but_malplaced:
            if word_wip.count(letter) < facit_letter_counts[letter]:
                word_wip[correct_but_malplaced.get(letter)] = f"({letter})"

        round += 1

        if word_wip == facit:
            game_status = "won"

        time.sleep(0.4)
        print()

    if game_status == "won":
        # Print the word being worked on:
        for letter in word_wip:
            print(letter, end=" ", flush=True)
            time.sleep(0.2)

        print("\n\nCongratulations! You guessed the word correctly within 5 rounds.\n")
        
    if game_status == "lost":
        # Print the word being worked on:
        for letter in word_wip:
            print(letter, end=" ", flush=True)
            time.sleep(0.2)

        print(f"\n\nGame over! You've run out of guessing rounds. The correct answer was: {word}\n")
    
    time.sleep(0.4)

def choose_word():
    """Choose a random word from the wordlist for the user to guess."""

    wordlist = open("wordlist.txt", "r")
    lines = wordlist.readlines()
    wordlist.close()

    num_of_words = len(lines)

    word_num = random.randint(0, num_of_words)
    word = lines[word_num].strip()

    return word

def main():
    """Start the Wordle module."""

    menu_loop()

if __name__ == "__main__":
    main()
