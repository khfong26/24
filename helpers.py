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

def is_solvable(nums_list):
    """Recursively checks if a list of numbers can make 24."""
    # Base case: if we've combined everything into one number, check if it's 24
    if len(nums_list) == 1:
        return math.isclose(nums_list[0], 24.0, abs_tol=1e-5)
    
    # Pick two numbers to combine
    for i in range(len(nums_list)):
        for j in range(len(nums_list)):
            if i == j: 
                continue
            
            # Create a list of the numbers we DIDN'T pick
            next_round = [nums_list[k] for k in range(len(nums_list)) if k != i and k != j]
            
            a, b = nums_list[i], nums_list[j]
            
            # Try all 4 operations, replacing the two numbers with the result, and recurse
            if is_solvable(next_round + [a + b]): return True
            if is_solvable(next_round + [a - b]): return True
            if is_solvable(next_round + [a * b]): return True
            
            # Prevent division by zero AND enforce clean, whole-number division
            if b != 0 and a % b == 0: 
                if is_solvable(next_round + [a / b]): return True
                
    return False

def get_four():
    """Draws 4 cards and verifies they can make 24. Redraws if they can't."""
    while True:
        # Draw 4 cards
        cards = [draw_card() for _ in range(4)]
        
        # Extract their numerical values using our map
        numeric_values = [VALUE_MAP[card.split(" of ")[0]] for card in cards]
        
        # If it works, break the loop and return them!
        if is_solvable(numeric_values):
            return cards

def share_cards():
    cards = session.get('cards', [])
    return [str(VALUE_MAP[card.split(" of ")[0]]) for card in cards]