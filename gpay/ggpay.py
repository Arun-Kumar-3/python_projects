user_dictionary=dict()
balance=dict()
viwe_statement=dict()

    


def split_amount(Name):
    Enter_split_amount=int(input("Enter the split amount : "))
    print("....The all users... :")

    for i,values in enumerate( user_dictionary.values()):
        print(i,values)
    
    

    Enter_users=input("Enter the users :").split(",")
    for i,values in enumerate(Enter_users):
        print(values ,end= ": ")
        enter_amount=int(input("enter the amount : "))
        if values==Name:
            current_amnt=Enter_split_amount-enter_amount
            balance.update({Name:current_amnt})
            viwe_statement.update({Name:current_amnt})
        else:
            balance.update({values:enter_amount})
            viwe_statement[values]=values+enter_amount
    print(balance) 
    print(viwe_statement)

def login():
    condition=True
    while condition==True:
        mobile_number=int(input("enter your mobile number : "))
        name=input("enter your name : ")
        
        if (mobile_number,name) in user_dictionary.items():
            check=True
            while check== True:
                print("1 . split amount \n2 . settle amount \n3 . viwe existing statements  \n0 . to exit")
                split_choice=int(input("Enter your Choice : "))
                if split_choice==1:
                    split_amount(name)
                elif split_choice==0:
                    check=False
                    condition=False
                elif split_choice==2:
                    settle()
        else:
            print("invalid input.mobile number or name is incorrect ")


choice = True
while choice == True:
    print(".................. welcome to the Google Pay ..............")
    print("1 . add user \n2 . login  \n0 . to exit")
    Enter_choice=int(input("Enter your choice : "))

    if Enter_choice==1:
        mobile_num=int(input("Enter your mobile number : "))
        name=input("enter your name : ")
        user_dictionary.update({mobile_num:name})
        print(user_dictionary)
        print(" 1 new user added ")
    elif Enter_choice==2:
        login()
    elif Enter_choice==0:
        choice=False

                                
