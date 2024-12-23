m=10
#print("   *")
#print("  ***")
#print(" *****")
#print("*******")
#Lst=["*********"," *******","  *****","   ***","    *"]
#Lst=Lst[::-1]
#for i in Lst:
#    print(i)
Lst=[]
index=0
for i in range(m,0,-1):
    if i%2!=0:
        b=len(Lst[index])
        if index==0:
            Lst.append("*"*i)
        if b < i:
            a=i/2
            Lst.append(f'{a*" "}{"*"*i}')
            index+=1
print(Lst)
    