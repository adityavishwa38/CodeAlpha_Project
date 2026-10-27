import random

words = ["One","Two","Three","Four","Five"]

secret_word = random.choice(words).lower()

guessed_letter = []
wrong_gyesses = 0
max_attempt = 6

print("="*35)
print("         Hangman Game")
print("="*35)

print("Guess the hidden word one letter at a time")
print("You have 6 incorrect guesses available")

while wrong_gyesses < max_attempt:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letter:
            display_word += letter + " "
        else:
            display_word += " "
            
    print("\nWord: ",display_word)
    print("Incorrect word: ",wrong_gyesses)
    print("Attempts remaining: ",max_attempt - wrong_gyesses)

    if all(letter in guessed_letter for letter in secret_word):
        print("\nCongratulations!! You guessed the word")
        print("The word was: ",secret_word)
        break
    
    guess = input("Enter one letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter!. Please enter one letter: ")
        continue
    
    if guess in guessed_letter:
        print("You already guessed that letter! Try again.")
        continue
    
    guessed_letter.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_gyesses += 1
        print("Wrong guess!!")
        

if wrong_gyesses == max_attempt:
    print("\nGame Over!!.. You have used all 6 incorrect guesses")
    print("The correct word: ",secret_word)