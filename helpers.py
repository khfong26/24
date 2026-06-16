import random
import math
from flask import session

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
nums = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

# Global mapping so it can be used for both math validation and sharing
VALUE_MAP = {
    "Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, 
    "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, 
    "Jack": 11, "Queen": 12, "King": 13
}

def shuffle_deck():
    new_deck = [num + " of " + suit for suit in suits for num in nums]
    random.shuffle(new_deck)
    return new_deck 

def draw_card():
    deck = session.get('deck', [])
    if not deck:
        deck = shuffle_deck()
    card = deck.pop()
    session['deck'] = deck
    return card

def _solve_24_all(nums_list):
    """Recursively finds ALL valid expressions that evaluate to 24."""
    if len(nums_list) == 1:
        final_value, final_expression = nums_list[0]
        if math.isclose(final_value, 24.0, abs_tol=1e-5):
            return {final_expression}
        return set()
    
    valid_solutions = set()
    
    for i in range(len(nums_list)):
        for j in range(len(nums_list)):
            if i == j: 
                continue
            
            next_round = [nums_list[k] for k in range(len(nums_list)) if k != i and k != j]
            
            val_a, expr_a = nums_list[i]
            val_b, expr_b = nums_list[j]
            
            # Addition
            valid_solutions.update(_solve_24_all(next_round + [(val_a + val_b, f"({expr_a} + {expr_b})")]))
            # Subtraction
            valid_solutions.update(_solve_24_all(next_round + [(val_a - val_b, f"({expr_a} - {expr_b})")]))
            # Multiplication
            valid_solutions.update(_solve_24_all(next_round + [(val_a * val_b, f"({expr_a} * {expr_b})")]))
            # Division
            if val_b != 0 and val_a % val_b == 0: 
                valid_solutions.update(_solve_24_all(next_round + [(val_a / val_b, f"({expr_a} / {expr_b})")]))

    return valid_solutions

def get_all_24_solutions(cards):
    """Wrapper function to format input and output."""
    starting_tuples = [(num, str(num)) for num in cards]
    solutions_set = _solve_24_all(starting_tuples)
    return sorted(list(solutions_set))

def get_four():
    """Draws 4 cards and verifies they can make 24. Returns the cards AND their solutions."""
    while True:
        # Draw 4 cards
        cards = [draw_card() for _ in range(4)]
        
        # Extract their numerical values using our map
        numeric_values = [VALUE_MAP[card.split(" of ")[0]] for card in cards]
        
        # Get the list of all possible math solutions
        solutions = get_all_24_solutions(numeric_values)
        
        # If the list is not empty, it's a valid hand! Break the loop and return both.
        if solutions:
            return cards, solutions

def share_cards():
    cards = session.get('cards', [])
    return [str(VALUE_MAP[card.split(" of ")[0]]) for card in cards]