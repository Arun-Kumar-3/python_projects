#
newword=input("Enter the words : ")



def check(newword):
    all_charecter=""
    i=0
    while i< len(newword):
        char=newword[i]
        count=1
        while i+1 < len(newword) and newword[i+1]==char:
        
            count+=1
            i+=1
        if count > 1:
            all_charecter+=char+str(count)
        else:
            all_charecter+=char
        
        i+=1
    return all_charecter


final=check(newword)
print(final)




#def check(letword):
 ##   Lst=[]
 #   recount=1
 #   for i in letword:
 #       
 #       
 #       if i not in Lst:
#            
 #           Lst.append(i)
  #          print("apended i : ",i)
       
  #      else:
   #         a=len(Lst)
   #         print("a is:",a)
   #         Lst.append(recount)
   #         Lst[a]=recount
   #         recount+=1
   # return Lst

#final=[]
#for k in newword:
 #   check[k]
 #   final.append(k)
#
#f#or j in final:
  #  print(j,end="")
    
    







#def check(letword):
#    Lst=[]
#    count=[]
#    for charecter in letword:
#        
#        lenth=len(count)
#        if charecter not in Lst:
#             
#                
#                Lst.append(lenth)
#                print("the charecter is",charecter)
#                Lst.append(charecter)
#            
#        else:
#            print("the else charecter is :",charecter )
 #           
#            count.append(charecter)
#            print("the count is :",count)
            
            
        #elif charecter in Lst and Lst[a] == 2 or Lst[a] == 2:
         #   Lst[a]=count+1
         #   count+=1
       # elif charecter in Lst:
        #    Lst.append(count)
            #else:
             #   Lst.append(2)
            
            
         #   a=len(Lst)-1
         #   print(Lst[a])
         #   if Lst[a] != 2 :
         #       Lst.append(2+count)
         #       count+=1
         #       
         #   else:
         #      Lst.append(2)
            #if a ==2:
              #Lst.append(2+count)
             # count+=1
            #else:
            
    #print(Lst[0 +1])
        
   
   
