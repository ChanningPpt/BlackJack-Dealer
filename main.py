import random

player_name = input("Type in your name here: ")

deck = [
    ['A♡', 11], ['2♡', 2], ['3♡', 3], ['4♡', 4], ['5♡', 5], ['6♡', 6], ['7♡', 7], ['8♡', 8], ['9♡', 9], ['10♡', 10], ['Jack♡', 10], ['Queen♡', 10], ['King♡', 10],
    ['A♢', 11], ['2♢', 2], ['3♢', 3], ['4♢', 4], ['5♢', 5], ['6♢', 6], ['7♢', 7], ['8♢', 8], ['9♢', 9], ['10♢', 10], ['Jack♢', 10], ['Queen♢', 10], ['King♢', 10],
    ['A♤', 11], ['2♤', 2], ['3♤', 3], ['4♤', 4], ['5♤', 5], ['6♤', 6], ['7♤', 7], ['8♤', 8], ['9♤', 9], ['10♤', 10], ['Jack♤', 10], ['Queen♤', 10], ['King♤', 10],
    ['A♧', 11], ['2♧', 2], ['3♧', 3], ['4♧', 4], ['5♧', 5], ['6♧', 6], ['7♧', 7], ['8♧', 8], ['9♧', 9], ['10♧', 10], ['Jack♧', 10], ['Queen♧', 10], ['King♧', 10]
]

random.shuffle(deck)

def deal_cards(deck, hand):
    card = deck.pop()
    hand.append(card)

def calculate_hand_value(hand):
    has_ace = False

    hand_value = int(hand[0][1]) + int(hand[1][1])

    if hand[0][0] or hand[1][0] == ['A♡', 'A♢', 'A♤','A♧']:
        has_ace = True
    
    if has_ace == True and hand_value > 21:
        hand_value -= 10
    
    print(player_name + "'s hand value: " + str(hand_value))

player_hand = []
dealer_hand = []

for i in range(2):
    deal_cards(deck, player_hand)
    deal_cards(deck, dealer_hand)

print(player_name + "'s hand: " + f"{player_hand}")
calculate_hand_value(player_hand)
print(f"Dealer hand: [{dealer_hand[0]}, <face down>]")