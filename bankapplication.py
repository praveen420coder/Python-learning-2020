data={1001:{'name':'Praveen','Passward':'pr12345','Balance':5674,'email':'sutharpks2658003@gmail.com','ph_no':'7023972612'},
      1002:{'name':'mayank','Passward':'my12345','Balance':7000,'email':'sainiunom@gmail.com','ph_no':'800567804'},
}
import sys
import time
def main():
    print('WELCOME TO WESTERN BANK OF INDIA',centre(50,'*'))
    print('1.LOGIN\n2.SIGN UP\n3.EXIT')
    time.sleep(3)
    user=int(input('Enter your choice:'))
    if user==1:
       login()
    elif user==2:
       signup()
    elif user==3:
       sys.exit()         

def login():
    print('WELCOME TO LOGIN PAGE:')
    acc=int(input('Enter your user id:'))
    if acc in data.keys():
       Passward=input('Enter your password:')
       if data[acc]['Passward']==Passward:
          print('..')
          time.sleep(1)
          print('..')
          time.sleep(1)
          print('WELCOME {data[acc][name]} YOU ARE LOGGED IN.....')
          time.sleep(3)
          print('1.CREDIT\n2.DEBIT\n3.CHEAK_BALANCE\n4.EXIT')
          usr=int(input('Enter your choice:'))
          if usr==1:
             credit(acc)
          elif usr==2:
             debit(acc)
          elif usr==3:
             cheak_balance(acc)
          elif usr==4:
             sys.exit() 
          else:
             print('INVAILD CHOICE')
       else:
           print('PASSWORD DOES NOT MATCH.')
           login()
    else:
       print('USER ID NOT MATCH.')
       main()