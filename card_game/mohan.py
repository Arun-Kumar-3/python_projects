

class CardHelper:
    def __init__(self):
        # self.players_name_list = input("Please enter player list : ").split(",")
        self.players_name_list = "gp,mohan,arun,haarish,dinesh".split(",")
        self.player_cards = {}
        for player in self.players_name_list:
            self.player_cards[player] = []
        self.deck = {"S":[],"C":[],"D":[],"H":[]}
        self.player_order_list = []
        self.current_cards = []
        self.current_max = None
        self.current_player_max_index = None
        self.shuffle_the_cards()

    def get_initial_card(self):
        if self.current_cards:
            return self.current_cards[0]
        raise Exception()
    
    def shuffle_the_cards(self):
        player_index = int(input("Enter Player index : "))
        self.player_order_list = self.players_name_list[player_index:] + self.players_name_list[:player_index]
        print(self.player_order_list)
        index = 0
        for _ in range(52):
            self.player_cards[self.player_order_list[index]].append('*')
            if index >= len(self.player_order_list)-1:
                index = 0
            else:
                index+=1

    def update_card(self, player, cards, extend=True):
        if extend:
            self.player_cards[player].extend(cards)
        else:
            self.player_cards[player][0] = cards[0]

    def remove_card(self, player, card):
        if card in self.player_cards[player]:
            self.player_cards[player].remove(card)
        else:
            self.player_cards[player].pop()

    def get_max_player(self, player_index, card):
        if self.current_max is None:
            self.current_max = card
            self.current_player_max_index = player_index
            return player_index
        if int(self.current_max[1:]) > int(card[1:]):
            return self.current_player_max_index
        else:
            self.current_player_max_index = player_index
            self.current_max = card

    def start_game(self, player_index = None):
        self.current_cards = []
        self.current_max = None
        self.current_player_max_index = None
        if not player_index:
            player_index = int(input("Enter Player index : "))
        self.player_order_list = self.player_order_list[player_index:] + self.player_order_list[:player_index]
        self.update_card(self.player_order_list[0], ["S-A"], extend=False)
        for index, player in enumerate(self.player_order_list):
            card = input(f"Enter the card which {player} has dropped : ")
            self.current_cards.append(card)
            self.remove_card(player, card)
            self.get_max_player(index+1, card)
            if self.get_initial_card()[0] == card[0]:
                pass
            else:
                pass
            print(self.player_cards)
            print(self.deck)
        for current_card in self.current_cards:
            self.deck[current_card[0]].append(current_card)
        self.start_game(self.current_player_max_index)



obj = CardHelper()
print(obj.player_cards)
obj.start_game()