import random
full_deck = {
    "club": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "spade": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "diamond": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
    "heart": [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
}

assistant = {"spade": [], "heart": [], "club": [], "diamond": [], "removed": []}

players=int(input("enter how many palyers wil play : "))
player_hands=52//players

all_players_names=input("enter players names : ").split(" ")
print("all players : ",all_players_names)

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

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~  NOW START THE GAME  ~~~~~~~~~~~~~~~~~~~~")

spade_ace_num=random.randint(0,players-1)
spade_ace_player=all_players_names[spade_ace_num]
print("Spade Ace is now : ",spade_ace_player)
assistant['spade'].append(f"{spade_ace_player} Spade A ")
print(assistant)

def players_play_order(start_index):
    return all_players_names[start_index:] + all_players_names[:start_index]

round_order = players_play_order(spade_ace_num)
print("round order: ",round_order)

def the_game(round_order):
    while player_hands > 1:  # Continue until only one player has cards
        all_card_entries = []
        different_symbol = False

        # Collect cards for the round
        for player_index, player in enumerate(round_order):
            card = input(f"{player}, enter your card (symbol number): ").split(" ")
            symbol, number = card[0].lower(), card[1].upper()
            value = card_value(number)
            all_card_entries.append((player,symbol,value))

            print("All card entries is : ",all_card_entries)
            #print("the if block is : ",all_card_entries[symbol])

            #for index,i in enumerate(all_card_entries[0]):
             #   print("~~~~~~~~ index and i is : ",index,i)

            if all_card_entries and all_card_entries[0][1] != symbol:
                different_symbol = True
                print("********************************diffrent card : ")
                break
               

        if  different_symbol==True:
            split_card_entries=all_card_entries[:len(all_card_entries)-1]
            print("the split card is : ",split_card_entries)
            #winning_card = max(split_card_entries, key=lambda x: card_value(x[0]))
            #print("the winning card is: ",winning_card)
            print("All card entries is : ",all_card_entries)
        else:
            print("all card entries :  ",all_card_entries)
            print("All card entery : ",all_card_entries[0][2]) 
            winning_card = max(all_card_entries, key=lambda x: card_value(x[2]))
            print("the winning card is : ",winning_card)
            for i in all_card_entries:
                if all_card_entries[i][2]==winning_card:
                    



the_game(round_order)
