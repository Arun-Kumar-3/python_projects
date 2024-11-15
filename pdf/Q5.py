word1=input("enter word 1: ")

word2=input("enter word 2 : ")

word1_set=set(word1).difference(set(word2))
word2_set=set(word2).difference(set(word1))


out=[]
for i in word1:
    if i in word1_set:
        out.append(i)
for j in word2:
    if j in word2_set:
        out.append(j)

for k in out:
    print(k,end="")