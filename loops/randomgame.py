import random
num = random.randint(1,49)
tries=0
while True:
    a=int(input("please enter the number between 1 and 49:- "))
    if num==a:
      print(f"you won the game in {tries} steps")
      tries+=1
      break
    elif num>a:
          print("go little higher")
          tries+=1
    elif  num<a:
          print("go little lower")
          tries+=1
    else:
         print("you loss") 
         tries+=1
 
