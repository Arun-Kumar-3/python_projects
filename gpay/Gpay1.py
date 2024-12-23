dictionary=dict()
Amount=dict()
viwe_statement=dict()
def split_amount(Name):
    print("the name is :",Name)

    Enter_split_amount=int(input("Enter the split amount : "))
    viwe_statement.update({Name:Enter_split_amount})
    print("....The all users... :")
    for values in dictionary.values():
        print(values)
    pre_amount=[]
    for pre in Amount.values():
        pre_amount.append(pre)

    Enter_users=input("Enter the users :").split(",")
    for i,values in enumerate(Enter_users):
        print(values ,end= ": ")
        enter_amount=int(input("enter the amount : "))
        if len(pre_amount) < 1:
            Amount.update({values:enter_amount})
        else:
            Amount.update({values:pre_amount[i] + enter_amount})
    print(Amount)
    print(viwe_statement)
    
   

def settle():
    
    settle_users=input("Enter you want to  settle users : ").split(",")
    pre_amount=[]
    for pre in Amount.values():
        pre_amount.append(pre)

    for i,values in enumerate(settle_users):
        print(values, end=": ")
        settle_amount=int(input("Enter the settle amount : "))
        Amount.update({values:pre_amount[i] - settle_amount})
    print(Amount)





def login():
        condition=True
        while condition==True:
            mobile_number=input("enter your mobile number : ")
            Name=input("enter your name : ")
            
            if (mobile_number,Name) in dictionary.items():
                check=True
                while check== True:
                    print("1 . split amount \n2 . settle amount \n3 . viwe existing statements  \n0 . to exit")
                    split_choice=int(input("Enter your Choice : "))
                    if split_choice==1:
                        split_amount(Name)
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
        mobile_num=input("Enter your mobile number : ")
        name=input("Enter your name : ")
        dictionary.update({mobile_num:name})
        
        print(" 1 new user added ")
    elif Enter_choice==2:
        login()  
    
    elif Enter_choice==0:
        choice=False
    print(dictionary)
