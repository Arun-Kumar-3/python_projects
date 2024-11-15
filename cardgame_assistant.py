
player_names=input("enter player names : ").split(",")
spade_ace_goto=int(input("enter player number  who will spade ace : "))
spade_ace=spade_ace_goto-1
assistant={
            "spade" :[],
            "diamond":[],
            "heart":[],
            "club":[],
            "removed_spade":[],
            "removed_diamond":[],
            "removed_heart":[],
            "removed_club":[]
        }
s,d,h,c=len(assistant["spade"]),len(assistant["diamond"]),len(assistant["heart"]),len(assistant["club"])
assistant_count=s+d+h+c
#print(assistant_count)
#print("the player names is :",player_names)

def round(spade_ace):
    round_of=player_names[spade_ace:]+player_names[:spade_ace]
    #print("round of players : ",round_of)
    return round_of
rounds=round(spade_ace)
#print(rounds)
def check(number):
    if number=="A":
        return 14
    elif number == "K":
        return 13
    elif number == "Q":
        return 12
    elif number == "J":
        return 11
    else:
        return int(number)


def start_game(rounds):
    #print("inside of start game : ",rounds)
    
    #def new_round(index):
    #    rounds=rounds[index:]+rounds[:index]
     #   return rounds

    #rounds=new_round(index) 

    while assistant_count < 52:
        collect_cards=[]
        diffrent_symbol=False
        print("the round order is : ",rounds)
        i=0
        while i < len(rounds):
            #print("the i is :",i)
            card=input(f"{rounds[i]} down your card or remove : ").split(" ")
            if card[0]=="remove":
                rounds.remove(rounds[i])
                i=i
                pass
            else:
                symbol=card[0]
                number=card[1]
                value=number
                collect_cards.append((rounds[i],symbol, value))
                if collect_cards[0][1] != symbol:
                    diffrent_symbol=True
                    break
                i+=1
        if diffrent_symbol==False:
            for j in collect_cards:
                
                if j[1]=="s":
                
                    assistant["removed_spade"].append(j[2])
                  
                elif j[1]=="d":
                    assistant["removed_diamond"].append(j[2])
                elif j[1]=="h":
                    assistant["removed_heart"].append(j[2])
                elif j[1]=="c":
                    assistant["removed_club"].append(j[2])

            for i in assistant["spade"]:
                #print("the i is : ",i)
                for k in assistant["removed_spade"]:
                    #print("k is : ",k[1])
                    #print("i of [1][1] is : ",i[1][1])
                    if i[1][1] == k:
                        
                        assistant["spade"].remove(i)

            for i in assistant["diamond"]:
                #print("the i is : ",i)
                for k in assistant["removed_diamond"]:
                    #print("k is : ",k[1])
                    #print("i of [1][1] is : ",i[1][1])
                    if i[1][1] == k:
                        
                        assistant["diamond"].remove(i)

            for i in assistant["heart"]:
                #print("the i is : ",i)
                for k in assistant["removed_heart"]:
                    #print("k is : ",k[1])
                    #print("i of [1][1] is : ",i[1][1])
                    if i[1][1] == k:
                        
                        assistant["heart"].remove(i)

            for i in assistant["club"]:
                #print("the i is : ",i)
                for k in assistant["removed_club"]:
                    #print("k is : ",k[1])
                    #print("i of [1][1] is : ",i[1][1])
                    if i[1][1] == k:
                        
                        assistant["club"].remove(i)
            winning_card = max(collect_cards, key=lambda x: check(x[2]))
            print(winning_card)
            for index,card in enumerate(collect_cards):
                if winning_card==card:
                    rounds=rounds[index:]+rounds[:index]
                    break

            print("the updated assistant is :",assistant)
            

        elif diffrent_symbol==True:
            a=len(collect_cards)-1
            removed_diffrent_symbol=collect_cards[:a]
            #print("removed_diffrent_symbol",removed_diffrent_symbol)
            winning_card = max(removed_diffrent_symbol, key=lambda x: check(x[2]))
            print(winning_card)
            for index,card in enumerate(collect_cards):
                if winning_card==card:
                    rounds=rounds[index:]+rounds[:index]
                    #rounds=new_round(index+1)
                    print("round is :",rounds)
                    break

            def prev_removed(sym):
                print("the sym is : ",sym)
                for i in range(len(assistant[sym])):
                    for j in range(i+1,len(assistant[sym])):
                        print("the i is :",assistant[sym][i][1] )
                        print("the j is :",assistant[sym][j][1] )
                        if assistant[sym][i][1] ==assistant[sym][j][1] :
                            assistant[sym].remove(assistant[sym][i])
            
            for card in collect_cards:
                if card[1]=="s":
                    assistant["spade"].append((winning_card[0],card[1:]))
                    prev_removed("spade")
                    
                elif card[1]=="d":
                    assistant["diamond"].append((winning_card[0],card[1:]))
                    prev_removed("diamond")
                elif card[1]=="h":
                    assistant["heart"].append((winning_card[0],card[1:]))
                    prev_removed("heart")
                elif card[1]=="c":
                    assistant["club"].append((winning_card[0],card[1:]))
                    prev_removed("club")
            
            

            print("Assistant - ",assistant)

start_game(rounds)
print(assistant)