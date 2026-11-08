# This program simulates a state capital guessing game.
import random

def main():
    # Dictionary with 10 states and capitals
    capitals = {
        'Hawaii': 'Honolulu',
        'Wyoming': 'Cheyenne',
        'New Hampshire': 'Concord',
        'Indiana': 'Indianapolis',
        'Illinois': 'Springfield',
        'California': 'Sacramento',
        'Texas': 'Austin',
        'New York': 'Albany',
        'Florida': 'Tallahassee',
        'Ohio': 'Columbus'
    }
    
    correct = 0
    incorrect = 0
    state_list = list(capitals.keys())
    
    keep_playing = True
    while keep_playing:
        state = random.choice(state_list)
        correct_capital = capitals[state]
        
        # Match the exact prompt format from screenshot 1
        user_guess = input(f"What is the capital of {state}? (or enter 0 to quit): ").strip()
        
        if user_guess == '0':
            keep_playing = False
        else:
            if user_guess.lower() == correct_capital.lower():
                print("That is correct.")
                correct += 1
            else:
                print("That is incorrect.")
                incorrect += 1
                
    # Single-line summary print matched to screenshot 1
    print(f"You had {correct} correct responses and {incorrect} incorrect responses.")

if __name__ == '__main__':
    main()
