import random

# Initialize deck and assistant tracking
full_deck = {
    "club": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "spade": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "diamond": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "heart": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
}

# Assistant to track cards by symbol
assistant = {"spade": [], "heart": [], "club": [], "diamond": [], "removed": []}

# Number of players and player names
players = int(input("Enter number of players: "))
all_players_names = input("Enter player names: ").split(" ")
print("All players:", all_players_names)

# Initialize player hands
player_hands = [[] for _ in range(players)]
cards_nums = 52

# Distribute cards (using placeholders for simplicity)
while cards_nums > 0:
    for i in range(players):
        if cards_nums <= 0:
            break
        player_hands[i].append("*")
        cards_nums -= 1

print("Card shuffled successfully.")

# Randomly assign Spade Ace holder to determine play order
spade_ace_num = random.randint(0, players - 1)
spade_ace = all_players_names[spade_ace_num]
print("Spade Ace is assigned to:", spade_ace)
assistant["spade"].append(f"{spade_ace} holds Spade A")

# Determine play order based on Spade Ace holder
def players_play_order(start_index):
    return all_players_names[start_index:] + all_players_names[:start_index]

round_order = players_play_order(spade_ace_num)
print("Play order:", round_order)

# Convert face card to numeric values for comparison but store as strings
def card_value(number):
    if number == 'A':
        return 14
    elif number == 'K':
        return 13
    elif number == 'Q':
        return 12
    elif number == 'J':
        return 11
    return int(number)

# Game round function
def the_game(round_order):
    while len([hand for hand in player_hands if hand]) > 1:  # Continue until only one player has cards
        all_card_entries = []
        different_symbol = False

        # Collect cards for the round
        for player_index, player in enumerate(round_order):
            card = input(f"{player}, enter your card (symbol number): ").split(" ")
            symbol, number = card[0].lower(), card[1].upper()
            value = card_value(number)

            # Add card to all_card_entries regardless of symbol difference
            all_card_entries.append((symbol, number, player, player_index))

            # Check for symbol difference and stop further card collection if a difference is detected
            if all_card_entries and all_card_entries[0][0] != symbol:
                different_symbol = True
                break

        # Determine the winner and assign cards
        if different_symbol:
            # Find the card with the highest value among previous entries
            winning_card = max(all_card_entries, key=lambda x: card_value(x[1]))
            winning_symbol, winning_number, winning_player, winner_index = winning_card

            # Award all cards to the winner
            player_hands[winner_index].extend([entry[:2] for entry in all_card_entries])

            # Update assistant with each card's symbol, winning player's name, and card number
            for symbol, number, _, _ in all_card_entries:
                assistant[symbol].append(f"{winning_player} {symbol} {number}")

            # Reorder for the next round, starting with the winner
            round_order = players_play_order(winner_index)
        else:
            # All cards have the same symbol - add to removed pile
            assistant["removed"].extend([f"{symbol} {number}" for symbol, number, _, _ in all_card_entries])
            
            # Remove cards from corresponding symbol in assistant
            for symbol, number, _, player_index in all_card_entries:
                card_to_remove = f"{all_players_names[player_index]} {symbol} {number}"
                
                # Check if the card is in the removed pile and remove it from the symbol list
                if card_to_remove in assistant["removed"]:
                    assistant[symbol] = [card for card in assistant[symbol] if card != card_to_remove]
                    print("~~~~~~~~~~~````````assistant symbol is :",assistant[symbol])
            print("All cards were the same symbol. Moved to removed pile.")

        # No need to print player hands anymore
        print("Round results:")
        print("Cards played:", all_card_entries)
        print("Updated assistant tracking:", assistant)

# Run the game
the_game(round_order)
print("Final assistant state:", assistant)

how are you 
def new_func1():
    how are you

new_func1,hi() 
def new_func(hi):
    how are you

new_func(hi) 
how are you 
def hello():
    how are you

hello() 
how are you 
how are you 
def new_funchllo():
    how

new_funchllo() are you 
