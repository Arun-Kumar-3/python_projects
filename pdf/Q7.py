# global alphabet
# alphabet=['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=input(" enter the numbers : ").split(",")

for i in numbers:
    print(chr(int(i)+64),end="")