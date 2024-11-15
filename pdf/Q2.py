arr=[6,4,1,2,3,4,1,5]
sum=8
pair=False
for i in arr:
    for j in arr:
        if i !=j  and i+j==sum:
            print(i,j)
                
            arr.remove(j)
            pair=True
            break
           
if pair== False:
     print("no pairs found")





#while left < right:
 #   if left + right == sum:
 #       print(left,right)
 #       break
 #   elif left + right < sum:
 #       left+=1
 #   elif left + right > sum:
  #      right+= 1 
#else:
   # print("no pair found")
#for i in range(len(arr)):
    #print(arr[0] + arr[i])
#print(arr[0] + arr[4] )
#print(arr[0] + arr[3])
#print(arr[0] + arr[2])
#print(arr[0] + arr[1])
#print(arr[0] + arr[0])

