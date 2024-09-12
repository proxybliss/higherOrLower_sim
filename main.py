import random
from collections import defaultdict

# Function to get a random card (number between 2 and 14)
def get_random_card():
    return random.randint(2, 14)

# Dictionary to store the frequency of games with different correct guesses
guess_counts = defaultdict(int)

# Simulate 100000 games
for _ in range(100000):
    correct_guesses = 0
    game_over = False
    current_card = get_random_card()

    # Play the game until it loses
    while not game_over:
        # Guess based on the current card
        if current_card < 8:
            guess = "Higher"
        elif current_card > 8:
            guess = "Lower"
        else:
            guess = random.choice(["Higher", "Lower"])
        
        # Draw the next card
        next_card = get_random_card()

        # Check if the guess is correct
        if (guess == "Higher" and next_card > current_card) or (guess == "Lower" and next_card < current_card):
            correct_guesses += 1
            current_card = next_card
        else:
            game_over = True

    # Record the number of correct guesses for this game
    guess_counts[correct_guesses] += 1

# Output the results
print("Game Results (Number of correct guesses -> Frequency of games):")
for guesses, count in sorted(guess_counts.items()):
    print(f"{guesses} correct guesses: {count} games")
