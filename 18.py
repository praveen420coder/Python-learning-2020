from sys import exit
def gold_room():
 print("This room is full of gold,how much do you take.")
 
 next=input(">")
 if(next=="0" or "1"):
  how_much=int(next)
 else:
  dead("Man,learn to type a number.")
 if(how_much<50):
  print("Nice,you are not greedy,you win!")
  exit(0)
 else:
  dead("You geedy bastard")
  
def dead(why):
 print(why,"good job")


def start():
 print("now you are Entering in the gold room.")
 gold_room()
 
start()