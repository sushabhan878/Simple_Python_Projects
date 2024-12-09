import random
from Wordlist import words

# Dictionary of key : ()
hangman_art ={0: ("   ",
                  "   ",
                  "   "),
              1: (" o ",
                  "   ",
                  "   "),
              2: (" o ",
                  " | ",
                  "   "),
              3: (" o ",
                  "/| ",
                  "   "),
              4: (" o ",
                  "/|\\",
                  "   "),
              5: (" o ",
                  "/|\\",
                  "/  "),
              6: (" o ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guesses):
    print("**************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letter:
            print(f"You already guessed the letter {guess}")
            continue
        guessed_letter.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WINNNNN!")
            is_running = False
        
        elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
