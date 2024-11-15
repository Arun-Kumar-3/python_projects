import random
word=input("Enter the word : ")
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=random.randint(1,26)
print(f"{alpha[a]}{word[::-1]}")


# global rand_alpha
# rand_alpha=alpha[a]


# word1=word[::-1]
# print("word1 is",word1)
# for i in word1:
#     if i == word1[0]:
#         print(rand_alpha,end="")
#         print(i,end="")
        
#     else:
#         print(i,end="")

#print(rand_alpha)
#print("a is :",a)
#a=random.random(alpha)
#print(a)

#word=[]
#print(word)
#word[::-1]
#len=len(word) -1
#result=word[0]=rand_alpha
#print(result)
#print(rand_alpha)

#print(word[len])


    #if i == len(word)-1:
       # print(i)
        
    #else:
        #print(i)