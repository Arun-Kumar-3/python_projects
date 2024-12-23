
print("...................... Welcome to Google pay interface  ..........................")
print("1 . add user \n2 . login")
choice=int(input("Enter your choice : "))

class Split:
    def __init__(self,choice):
        self.choice=choice
    
    

    def user(self):
        global dic
        dic={}
        print(dic)
        if self.choice==1:
            mobile_num=input("enter your mobile number : ")
            name=input("enter your name : ")
            if mobile_num not in dic:
                dic.update({mobile_num:name})
        else:
                print("already user exists")

        print(dic)

    def Login(self):
        if choice==2 :
            mobile_num=input("enter your mobile number : ")
            name=input("enter your name : ")
        if (mobile_num ,name) in dic.items():
                print(f"......... Hi {name}.....")
                print("1 . split amount \n2 . settle amount \n3 .viwe existing statements ")
                next_choice=int(input("Enter Your Choice : "))
                print("the dictionary is",dic)
        else:
            print("invalid your mobile number or name  ")

    
obj=Split(choice)
obj.user()


            