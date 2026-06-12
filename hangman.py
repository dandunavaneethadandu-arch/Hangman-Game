import random

# Hangman stages
stages = [

"""
  -----
  |   |
      |
      |
      |
---------
""",

"""
  -----
  |   |
  O   |
      |
      |
---------
""",

"""
  -----
  |   |
  O   |
  |   |
      |
---------
""",

"""
  -----
  |   |
  O   |
 /|   |
      |
---------
""",

"""
  -----
  |   |
  O   |
 /|\\ |
      |
---------
""",

"""
  -----
  |   |
  O   |
 /|\\  |
 /    |
---------
""",

"""
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
---------
"""
]
# predefined words
word_list = ["apple", "banana", "orange", "tiger", "chair"]

lives = 6

print("🎯 Welcome to Hangman Game")

# random word choose
chosen_word = random.choice(word_list)

display = []

# blanks create
for _ in chosen_word:
    display.append("_")

guessed_letters = []

game_over = False

while not game_over:

    print("\nWord:", " ".join(display))

    guess = input("Guess a letter: ").lower()

    # already guessed check
    if guess in guessed_letters:
        print("⚠ Already guessed this letter")
        continue

    guessed_letters.append(guess)

    # correct guess check
    if guess in chosen_word:

        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        print("✅ Correct Guess!")

    else:
        lives -= 1
        print("❌ Wrong Guess")
        print("Remaining Chances:", lives)
        print(stages[6-lives])
    # win condition
    if "_" not in display:
        print("\n🎉 You Win!")
        print("Word was:", chosen_word)
        game_over = True

    # lose condition
    if lives == 0:
        print("\n💀 Game Over!")
        print("Correct Word:", chosen_word)
        game_over = True
        
