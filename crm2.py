from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv  
from tkinter import ttk


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("300x600")

mydb=mysql.connector.connect(
         host="localhost",
         user="root",
         port="3305",
         passwd="12345",
         database="codemy"
         

)


#print(mydb)
# create a cursor
my_cursor=mydb.cursor()

#my_cursor.execute("create database codemy")
#my_cursor.execute("show databases")
#for db in my_cursor:
 #print(db)
 
#my_cursor.execute("create table if not exists customers( first_name varchar(255), \
 #          last_name varchar(225),\
  #        zipcode int(10),\
   #       price_paid decimal(10,2),\
     #     user_id INT AUTO_INCREMENT PRIMARY KEY)") 
#my_cursor.execute("Alter table customers add(\
 #                email varchar(255),\
  #             state varchar(225),\
   #              country varchar(225),\
    #             pyment_method varchar(225),\
     #            discount_code varchar(225))")
     
     
#my_cursor.execute("Alter table customers add(\
 #             address varchar(255))")
def clear_flue():
  first_name_box.delete(0,END)
  last_name_box.delete(0,END)
  address_box.delete(0,END)
  city_box.delete(0,END)
  state_box.delete(0,END)
  country_box.delete(0,END)
  pyment_method_box.delete(0,END)
  zipcode_box.delete(0,END)
  user_id_box.delete(0,END)
  email_box.delete(0,END)
  phone_box.delete(0,END)
  discount_box.delete(0,END)
  price_paid_box.delete(0,END)
 
def add_cust():
  sql_command="insert into customers(first_name,last_name,address,city,state,country,pyment_method,zipcode,user_id,email,phone,discount_code,price_paid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  values=(first_name_box.get(),last_name_box.get(),address_box.get(),city_box.get(),state_box.get(),country_box.get(),pyment_method_box.get(),zipcode_box.get(),user_id_box.get(),email_box.get(),phone_box.get(),discount_box.get(),price_paid_box.get())
  my_cursor.execute(sql_command,values)
  
  
  
  
  mydb.commit()
  
  clear_flue()
def write_to_csv(result):
 with open('customer.csv','a')as f:
  w=csv.writer(f,dialect='excel')
  for record in result:
   w.writerow(record)
def searchcustomer():
 search_customer_query=Tk()
 search_customer_query.title("List All Customer")
 search_customer_query.iconbitmap('f:iron.ico')
 search_customer_query.geometry("800x800")
 def close():
  search_customer_query.destroy()
 def searchbox():
  selected=drop.get()
  if selected=="Search By..":
   text=Label(search_customer_query,text="You forget to pick").grid(row=3,column=0)
   return
  if selected=="Last Name":
   sql="select * from customers where last_name=%s"
  if selected=="Email":
   sql="select * from customers where email=%s"
  if selected=="User Id":
   sql="select * from customers where user_id=%s" 
  searched=search_box.get()
  #sql="select * from customers where last_name=%s"
  name=(searched,)
  result=my_cursor.execute(sql,name)
  result=my_cursor.fetchall()
  if not result:
    result="Record not Found.."
  my_frame=LabelFrame(search_customer_query,text="Searched Data",padx=150,pady=50)
  my_frame.grid(row=4,column=0,columnspan=2,pady=10)
  
  #searched_label=Label(my_frame,text=result)
  #searched_label.grid(row=14,column=0,padx=10,columnspan=2)
  first_name_box=Entry(my_frame)
  first_name_box.grid(row=1,column=1)
  last_name_box=Entry(my_frame)
  last_name_box.grid(row=2,column=1,pady=5)
  address_box=Entry(my_frame)
  address_box.grid(row=3,column=1,pady=5)
  city_box=Entry(my_frame)
  city_box.grid(row=4,column=1,pady=5)
  state_box=Entry(my_frame)
  state_box.grid(row=5,column=1,pady=5)
  country_box=Entry(my_frame) 
  country_box.grid(row=6,column=1,pady=5)
  pyment_method_box=Entry(my_frame)
  pyment_method_box.grid(row=7,column=1,pady=5)
  zipcode_box=Entry(my_frame)
  zipcode_box.grid(row=8,column=1,pady=5)
  user_id_box=Entry(my_frame)
  user_id_box.grid(row=9,column=1,pady=5)
  email_box=Entry(my_frame)
  email_box.grid(row=10,column=1,pady=5)
  phone_box=Entry(my_frame)
  phone_box.grid(row=11,column=1,pady=5)
  discount_box=Entry(my_frame)
  discount_box.grid(row=12,column=1,pady=5)
  price_paid_box=Entry(my_frame)
  price_paid_box.grid(row=13,column=1,pady=5)
  
  first_name_box.insert(0,result[0][0])
  last_name_box.insert(0,result[0][1])
  address_box.insert(0,result[0][12])
  city_box.insert(0,result[0][6])
  state_box.insert(0,result[0][8])
  country_box.insert(0,result[0][9])
  pyment_method_box.insert(0,result[0][10])
  zipcode_box.insert(0,result[0][2])
  user_id_box.insert(0,result[0][4])
  email_box.insert(0,result[0][5])
  phone_box.insert(0,result[0][7])
  discount_box.insert(0,result[0][11])
  price_paid_box.insert(0,result[0][3])
  
  
  
  
  
 search_box=Entry(search_customer_query)
 search_box.grid(row=0,column=1,padx=10,pady=10)
 search_customer_label=Label(search_customer_query,text="Search ")
 search_customer_label.grid(row=0,column=0,padx=10,pady=10)
 search_button=Button(search_customer_query,text="Search Customer",command=searchbox)
 search_button.grid(row=1,column=0,padx=10)
 
 drop=ttk.Combobox(search_customer_query,value=["Search By..","Last Name","Email","User Id"])
 drop.current(0)
 drop.grid(row=0,column=2)
 
def listcustomer():
 list_customer_query=Tk()
 list_customer_query.title("List All Customer")
 list_customer_query.iconbitmap('f:iron.ico')
 list_customer_query.geometry("800x600")
 my_cursor.execute("select * from customers ")
 result=my_cursor.fetchall()
 
 for index,x in enumerate(result):
  num=0
  for y in x:
   lookup_label=Label(list_customer_query,text=y)
   lookup_label.grid(row=index,column=num)
   num+=1
 csv_button=Button(list_customer_query,text="Save To Excel",command=lambda: write_to_csv(result))
 csv_button.grid(row=index+1,column=0)
  
  
  
title_label=Label(root,text="Customer Database",font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,pady=10)
f_name_l=Label(root,text="First Name").grid(row=1,column=0,sticky=W,padx=10)
l_name_l=Label(root,text="Last Name").grid(row=2,column=0,sticky=W,padx=10)
address_l=Label(root,text="Address").grid(row=3,column=0,sticky=W,padx=10)
city_l=Label(root,text="City").grid(row=4,column=0,sticky=W,padx=10)
state_l=Label(root,text="State").grid(row=5,column=0,sticky=W,padx=10)
country_l=Label(root,text="Country").grid(row=6,column=0,sticky=W,padx=10)
pyment_method_l=Label(root,text="Payment Method").grid(row=7,column=0,sticky=W,padx=10)
zipcode_l=Label(root,text="ZipCode").grid(row=8,column=0,sticky=W,padx=10)
user_id_l=Label(root,text="User_Id").grid(row=9,column=0,sticky=W,padx=10)
email_l=Label(root,text="Email").grid(row=10,column=0,sticky=W,padx=10)
phone_l=Label(root,text="Phone").grid(row=11,column=0,sticky=W,padx=10)
discount_code_l=Label(root,text="Discount Code").grid(row=12,column=0,sticky=W,padx=10)
price_paid_l=Label(root,text="Price Paid").grid(row=13,column=0,sticky=W,padx=10)
first_name_box=Entry(root)
first_name_box.grid(row=1,column=1)
last_name_box=Entry(root)
last_name_box.grid(row=2,column=1,pady=5)
address_box=Entry(root)
address_box.grid(row=3,column=1,pady=5)
city_box=Entry(root)
city_box.grid(row=4,column=1,pady=5)
state_box=Entry(root)
state_box.grid(row=5,column=1,pady=5)
country_box=Entry(root)
country_box.grid(row=6,column=1,pady=5)
pyment_method_box=Entry(root)
pyment_method_box.grid(row=7,column=1,pady=5)
zipcode_box=Entry(root)
zipcode_box.grid(row=8,column=1,pady=5)
user_id_box=Entry(root)
user_id_box.grid(row=9,column=1,pady=5)
email_box=Entry(root)
email_box.grid(row=10,column=1,pady=5)
phone_box=Entry(root)
phone_box.grid(row=11,column=1,pady=5)
discount_box=Entry(root)
discount_box.grid(row=12,column=1,pady=5)
price_paid_box=Entry(root)
price_paid_box.grid(row=13,column=1,pady=5)
add_b= Button(root,text="Add Data",command=add_cust)
add_b.grid(row=14,column=0,padx=10,pady=10)
clear_b= Button(root,text="Clear Fields",command=clear_flue)
clear_b.grid(row=14,column=1,padx=10,pady=10)
list_customer_button=Button(root,text="List Customer",command=listcustomer)
list_customer_button.grid(row=15,column=0, padx=10,pady=10)
search_customer_button=Button(root,text="Search Customer",command=searchcustomer)
search_customer_button.grid(row=15,column=1, padx=10,pady=10)




root.mainloop()