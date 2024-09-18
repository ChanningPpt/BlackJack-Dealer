import random

# Take user input for their player name.
player_name = input("Type in your name here: ")

# Deck of cards via a two-dimensional array.
deck = [
    ['A♡', 11], ['2♡', 2], ['3♡', 3], ['4♡', 4], ['5♡', 5], ['6♡', 6], ['7♡', 7], ['8♡', 8], ['9♡', 9], ['10♡', 10], ['Jack♡', 10], ['Queen♡', 10], ['King♡', 10],
    ['A♢', 11], ['2♢', 2], ['3♢', 3], ['4♢', 4], ['5♢', 5], ['6♢', 6], ['7♢', 7], ['8♢', 8], ['9♢', 9], ['10♢', 10], ['Jack♢', 10], ['Queen♢', 10], ['King♢', 10],
    ['A♤', 11], ['2♤', 2], ['3♤', 3], ['4♤', 4], ['5♤', 5], ['6♤', 6], ['7♤', 7], ['8♤', 8], ['9♤', 9], ['10♤', 10], ['Jack♤', 10], ['Queen♤', 10], ['King♤', 10],
    ['A♧', 11], ['2♧', 2], ['3♧', 3], ['4♧', 4], ['5♧', 5], ['6♧', 6], ['7♧', 7], ['8♧', 8], ['9♧', 9], ['10♧', 10], ['Jack♧', 10], ['Queen♧', 10], ['King♧', 10]
]

# Shuffle the deck.
random.shuffle(deck)

# Function used to deal cards that takes two arguments: one for the deck of cards, and the other for the player/dealer hand.
def deal_cards(deck, hand):
    card = deck.pop() # Randomly select a card from the deck.
    hand.append(card) # Adds the selected card to the player/dealer hand.

# Function used to calculate the hand value for the player/dealer.
def calculate_hand_value(hand):
    has_ace = False # Establish a boolean to see if the hand has an ace.

    # Calculate the hand value by taking the second object in the array from both cards and adding them together.
    hand_value = int(hand[0][1]) + int(hand[1][1]) 

    # Checks if either card is an ace.
    if hand[0][0] or hand[1][0] == ['A♡', 'A♢', 'A♤','A♧']:
        has_ace = True # Changes the boolean value to true.
    
    # Checks if the hand has an ace, and if the hand value is greater than or equal to 21.
    # Used to decide if the ace value should be 1 or 11.
    if has_ace == True and hand_value > 21:
        hand_value -= 10 # Subtracts 10 from the hand value if the conditions are met.

    return hand_value # Ends function, and returns the hand value back to the original variable.    

# Player and dealer hands as empty lists to store the dealt cards.
player_hand = []
dealer_hand = []

# Loops twice to deal cards out.
for i in range(2):
    deal_cards(deck, player_hand)
    deal_cards(deck, dealer_hand)

# Print out the player's hand and hand value, and the dealer hand.
print(f"{player_name}'s hand: {player_hand} ({calculate_hand_value(player_hand)})")
print(f"Dealer hand: [{dealer_hand[0]}, <face down>]")