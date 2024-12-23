import random

class Guess:
  def __init__(self,genarate,a=1,b=100):
    self.genarated_number=genarate
    self.a=a
    self.b=b
    print("self.genarated _number ",self.genarated_number)
  def game(self,genarated_new_value):
    guess_number=random.randint(1,100)
    print("guess number : ",guess_number)
    print("genarated number :",genarated_new_value)
    Lst=[]
    count=1
    while count < 4 :
      print("the genarated value is :",genarated_new_value)
      Lst.append(genarated_new_value)  
      next_value=Lst[0]  
      print("the next value is: ",next_value)

      #next_value=genarated_new_value
      #next_value=next_value1
      print(f"Attempt : {count}")
      if guess_number == next_value:
        print("YOU WON !")
        break

      elif guess_number < next_value:

          print("greater then")
          
          self.b=next_value
          

          if count==3 :
            print("YOU LOSE !")
      else:
          print("lesser then")
          self.a=next_value
          
          if count==3:
             print("YOU LOSE !")
      
      count+=1
      Lst[0]=modify(self.a,self.b)
      print(next_value)
  
def modify(a=1,b=100):
    print("type of a",type(a))
    print("a is",a)
    print("b is ",b)
    new_value=random.randint(a,b)
    return new_value


def genarate_num():
  genarate_num1=random.randint(1,100)
  print("genarate number ",genarate_num1)
  return genarate_num1

init_num=genarate_num()
#print("initial number",init_num)
obj=Guess(12)
#genarate_new_value=obj.modify()
#print("genarate_new_value",genarate_new_value)
obj.game(init_num)
