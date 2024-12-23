import random
import math

#full_deck[0] = club, full_deck[1]= spade, full_deck[2]= dimond, full_deck[3] = heart
full_deck=[[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A']]

#create assistant 
#[0]=Spade , [1]= heart , [2]= clever  , [3] = diomand ,[4] = ramoved cards 
assistant=[[],[],[],[],[]]






players=int(input("enter how many palyers wil play : "))

all_players_names=input("enter players names : ").split(" ")
print("all players : ",all_players_names)

separate_list=[]
for i in range(players):
    separate_list.append(list())
    
#print(separate_list)

cards_nums=52
while cards_nums > 1:
    if cards_nums > players:
        for j in range(players):
            separate_list[j].append("*")
        #print("before split ",separate_list)
        cards_nums-=players
    else:
        for k in range(cards_nums):
            separate_list[k].append("*")
            #print("else part of cards : ",separate_list)
        cards_nums-=cards_nums
print("Card shuffled succesfully ..........")
print(separate_list)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~  NOW START THE GAME  ~~~~~~~~~~~~~~~~~~~~")

spade_ace_num=random.randint(0,players-1)
spade_ace=all_players_names[spade_ace_num]
print("Spade Ace is now : ",spade_ace)
assistant[0].append(f"{spade_ace} Spade A ")
print(assistant)



def players_play(spade_ace_num):
    round_of_paai=[]
    if spade_ace_num < len(all_players_names):
        add_num=spade_ace_num
        while add_num < len(all_players_names):
            round_of_paai.append(all_players_names[add_num])
            add_num+=1
    for name in range(spade_ace_num):
        round_of_paai.append(all_players_names[name])
    
    print(round_of_paai)
    return round_of_paai

round_of_paai=players_play(spade_ace_num)

def the_game(round_of_paai):
    all_card_symbol=[]
    all_card_number=[]
    all_card_symbol_number=[]

    def send_card():
        print("All card number is ----- : ",all_card_symbol_number)
        'A'==14
        'K'==13
        'Q'==12
        'J'==11
        biggest=0
        count=0
        while count < len(all_card_symbol_number):
            if int(all_card_symbol_number[count][1]) > biggest:
                biggest+=int(all_card_symbol_number[count][1])
            count+=1
        print("the biggest number is : ",biggest)

        for index,check in enumerate(all_card_symbol_number):
            if int(check[1])==biggest:
                separate_list.pop()
                separate_list[index].extend(all_card_symbol_number)
                
                for each,name in zip(all_card_symbol_number,round_of_paai):
                    if each[0] =="spade":
                        assistant[0].append(f'{name} {each} ')
                    elif each[0] == "heart":
                        assistant[1].append(f'{name} {each} ')
                    elif each[0] == "cleaver":
                        assistant[2].append(f'{name} {each} ')
                    elif each[0]== "dimand":
                        assistant[3].append(f'{name} {each} ')
        
                
        print(separate_list)
        print(assistant)



        



    player=0
    while player < len(round_of_paai):
        print(f"{round_of_paai[player]} down your card : ")
        symbol_and_num=input("Enter card symbol & num : ").split(" ")
        symbol=symbol_and_num[0]
        number=symbol_and_num[1]
        if symbol not in all_card_symbol and player >= 1:
            all_card_symbol.append(symbol)
            all_card_number.append(number)
            all_card_symbol_number.append(symbol_and_num)
            send_card()
            break
        else:
            all_card_symbol.append(symbol)
            all_card_number.append(number)
            all_card_symbol_number=[symbol_and_num]
    

        player+=1

    print(all_card_symbol)
    print(all_card_number)

  


    def remove_card():
        for symb,num in zip(all_card_symbol,all_card_number):
            assistant[4].append(f"{symb} {num}")

   

    




the_game(round_of_paai)

print(assistant)
# arun haris mohan gp