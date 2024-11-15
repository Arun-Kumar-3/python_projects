user_data={}
print_split={}
all_user_transaction={}
settle_users={}

def add_user():
    mobile=int(input("Enter your mobile number : "))
    name=input("Enter your name : ")
    user_data[mobile]=name

    print(user_data)


def split_amount(name):
    total_spllit_amount=int(input("enter total split amount : "))
    print("......... all users ......")
    if name not in all_user_transaction:
        all_user_transaction[name]={}
    #print("####",all_user_transaction)
    for i in user_data.values():
        print(i)
    Enter_users=input("Enter users you want to split : ").split(" ")
    print(Enter_users)
    for user in Enter_users:

        # create user name for settle
        if user not in settle_users:
            settle_users[user]={}

        print(f'{user} - ',end="")
        enter_amount=int(input("enter the amount : "))
        if user==name:
            print_split.update({user:enter_amount})
            pass
        
        else:
            

            if user in all_user_transaction[name]:
                all_user_transaction[name][user]+=enter_amount
                #settle_users[user][name]-=enter_amount
                #all_user_transaction[user][name]-=enter_amount
                print_split.update({user:enter_amount})
            
            else:
                all_user_transaction[name][user]=enter_amount
                print_split.update({user:enter_amount})

            if user==name:
                print_split.update({user:enter_amount})
                pass
            else:
                
                if name in settle_users[user]:
                    settle_users[user][name]+=enter_amount
                    #print("the user :",{user})
                    #print(f"the name : {name}")
                    #settle_users[name][user]-=enter_amount
                    #all_user_transaction[name][user]-=enter_amount
                else:
                    settle_users[user][name]=enter_amount

            if name in settle_users and user in all_user_transaction:
                #print("the user :",{user})
                #print(f"the name : {name}")
                settle_users[user][name]-=enter_amount
                settle_users[name][user]-=enter_amount

                all_user_transaction[user][name]-=enter_amount
                all_user_transaction[name][user]-=enter_amount

            
            #if user==name:
            #    print_split.update({user:enter_amount})
            #    pass
            #else:
            #    if name in settle_users[user]:
            #        settle_users[user][name]-=enter_amount
            #    if user in all_user_transaction[name]:
            #        all_user_transaction[name][user]-=enter_amount

    print("splited persons : ",print_split ,"split successfully")      
    #print(all_user_transaction)
    #print("## settle amount is : ",settle_users)
        

def settle_amount(name):
    print("you pending to settle this users.....")
    print(settle_users[name])
    enter_settle_user=input("Enter user name you want to settle : ").split()
    print(enter_settle_user)
    for user in enter_settle_user:
        print(f'{user} --',end="" )
        enter_settle_amount=int(input("Enter the amount : "))
        settle_users[name][user]-=enter_settle_amount
        all_user_transaction[user][name]-=enter_settle_amount
        print("amount settled succesfully")

    


def viwe_balance(name):
    if name not in all_user_transaction:
        all_user_transaction[name]={}
        print("Pay to you : ",all_user_transaction[name])
    else:
        print("Pay to you : ",all_user_transaction[name])
    if name not in settle_users:
        settle_users[name]={}
        print("Pay by YOU :",settle_users[name])
    else:
        print("Pay by YOU :",settle_users[name])

def user_login():
    prompt2=True
    while prompt2==True:

        mobile=int(input("Enter your mobile number : "))
        name=input("Enter your name : ")
        if mobile in user_data and name in user_data.values():
            prompt3=True
            while prompt3==True:
                print("1 . split amount \n2 . settle \n3 .viwe balance \n0 . to exit ")
                choice2=int(input("Enter your choice : "))
                if choice2==1:
                    split_amount(name)
                elif choice2==2:
                    settle_amount(name)
                elif choice2==3:
                    viwe_balance(name)
                elif choice2==0:
                    print("/************* exit **********/")
                    prompt2=False
                    prompt3=False
                else:
                    print("invalid choice ")
        else:
            print("mobile number or name is incorrect...")        
    

prompt1=True
while prompt1==True:
    print(".................... welcome to google pay .................")
    print("1 . add user \n2 . user login  \n0 . to exit ")
    choice=int(input("Enter your choice : "))

    if choice == 1:
        add_user()
    elif choice== 2:
        user_login()
    elif choice==0 :
        print("................... exit .................")
        prompt1=False
    else:
        print("invalid choice ")

#print(all_user_transaction)
#print(settle_users)