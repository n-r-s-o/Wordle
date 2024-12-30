# Wordle

import random

# Create a text file of words that are 5 letters long
# The function only needs to be run once
def initialize_wordlist():
    str_list = []
    
    with open("3000-common-words.txt", "r") as wordlist:
        for word in wordlist:
            word = word.strip()

            if len(word) == 5 and word[0].islower():
                str_list.append(word)

    new_wordlist = open("5-letter-words.txt", "w")

    num_of_words = len(str_list)

    i = 0

    # Write words from the list of strings until there's just one left
    while i < num_of_words - 1:
        new_wordlist.write(str_list[i] + "\n")
        i += 1

    # Write the last word without a new line
    new_wordlist.write(str_list[i])

    new_wordlist.close()

def menu_loop():
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
    word = choose_word()

    word_wip = {
        1: "_ ",
        2: "_ ",
        3: "_ ",
        4: "_ ",
        5: "_ "
    }

    facit = {
        1: word[0:1],
        2: word[1:2],
        3: word[2:3],
        4: word[3:4],
        5: word[4:5]
    }

    # Print the correct answer:
    # for letter in facit.values():
    #     print(letter, end=" ")
    # print()

    guesses = []
    round = 1
    game_status = "running"
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    wordlist = open("5-letter-words.txt", "r").readlines()

    while game_status == "running":
        # Print the word being worked on:
        for letter in word_wip.values():
            print(letter, end="")
        print()

        if round == 5:
            game_status = "lost"

        print("Letters to guess from: ")
        for letter in alphabet:
            print(letter, end=" ")
        print()

        guess = input("Guess a word: ").lower().strip()

        if not guess.isascii():
            print("Invalid character(s).")

        elif len(guess) == 5:
            print("Guessed word must be 5 letters.")
        
        elif guess in guesses:
            print("You've already guessed that word.")

        elif guess not in wordlist:
            print("Word does not exist in the wordlist.")
            
        else:
            for guessed_letter in guess:
                for correct_letter in facit.values():
                    if guessed_letter == correct_letter:
                        # do stuff
                        pass

            guesses.append(guess)
            round += 1

        if word_wip != facit:
            game_status = "won"

def choose_word():
    wordlist = open("5-letter-words.txt", "r")
    lines = wordlist.readlines()
    wordlist.close()

    num_of_words = len(lines)

    word_num = random.randint(0, num_of_words)
    word = lines[word_num].strip()

    return word

def main():
    # If you're running the game for the first time:
    # initialize_wordlist()

    #menu_loop()
    game()

if __name__ == "__main__":
    main()
