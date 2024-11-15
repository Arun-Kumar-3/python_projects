import random
subject=input("Enter the subjects : ").split(",")
#subject=["tamil   ","english ","maths   ","science ","social  "]
days=int(input("Enter the days : "))
hours=int(input("Enter the hours : "))
sub_len=len(subject)
for i in range(days):
    for j in range(hours):
        random_number=random.randint(0,sub_len-1)
        print(subject[random_number],end=" | ")

    print(" ")

# tamil   ,english ,maths   ,science ,social   ,