data={1001:{'name':'Praveen','Passward':'pr12345','Balance':5674,'email':'sutharpks2658003@gmail.com','ph_no':'7023972612'},
      1002:{'name':'mayank','Passward':'my12345','Balance':7000,'email':'sainiunom@gmail.com','ph_no':'800567804'},
}
import sys
import time
def main():
  print("WELCOME TO WESTERN BANK OF INDIA",centre(50,'*'))
  print('1.LOGIN\n2.SIGN UP\n3.EXIT')
  time.sleep(3)
  user=int(input('Enter your choice:'))
  if user==1:
    login()
  elif user==2:
    signup()
  else:
    sys.exit()         