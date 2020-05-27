from tkinter import *
from PIL import ImageTk,Image
import sqlite3



root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("370x400")



#crate Table
 
conn=sqlite3.connect('address_book.db')

  # create cursor
c=conn.cursor()
  

#c.execute("""CREATE TABLE addresses(first_name text,last_name text,address text,city text,state text,zipcode integer)""")

def update():
 conn=sqlite3.connect('address_book.db')

  # create cursor
 c=conn.cursor()

 record_id=delete_box.get()
 c.execute(""" UPDATE addresses SET 
              first_name=:first,
              last_name=:last,
              address=:address,
              city=:city,
              state=:state,
              zipcode=:zipcode
                  
              WHERE oid=:oid""",
              {
               'first':f_name_e.get(),
               'last':l_name_e.get(),
               'address':address_e.get(),
               'city':city_e.get(),
               'state':state_e.get(),
               'zipcode':zipcode_e.get(),
               'oid':record_id
              
              
              
              }
 
    )


      #commit changes
 conn.commit()

     #closed connection
 conn.close()
  
 editor.destroy()



def edit():
 global editor
 
 editor=Tk()
 editor.title("Update a Record")
 editor.iconbitmap('f:iron.ico')
 editor.geometry("300x200")
 conn=sqlite3.connect('address_book.db')

  # create cursor
 c=conn.cursor()
 record_id=delete_box.get()
 c.execute("SELECT * FROM addresses WHERE oid="+record_id)
 record=c.fetchall()
 global f_name_e
 global l_name_e
 global address_e
 global city_e
 global state_e
 global zipcode_e
  
 f_name_e=Entry(editor,width=30)
 f_name_e.grid(row=0,column=1,padx=20,pady=(10,0))


 l_name_e=Entry(editor,width=30)
 l_name_e.grid(row=1,column=1,padx=20)


 address_e=Entry(editor,width=30)
 address_e.grid(row=2,column=1,padx=20)


 city_e=Entry(editor,width=30)
 city_e.grid(row=3,column=1,padx=20)


 state_e=Entry(editor,width=30)
 state_e.grid(row=4,column=1,padx=20)


 zipcode_e=Entry(editor,width=30)
 zipcode_e.grid(row=5,column=1,padx=20)

 f_name_l=Label(editor,text="First Name")
 f_name_l.grid(row=0,column=0,pady=(10,0))
 l_name_l=Label(editor,text="Last Name")
 l_name_l.grid(row=1,column=0)
 address_l=Label(editor,text="Address")
 address_l.grid(row=2,column=0)
 city_l=Label(editor,text="city")
 city_l.grid(row=3,column=0)
 state_l=Label(editor,text="state")
 state_l.grid(row=4,column=0)
 zipcode_l=Label(editor,text="zipcode")
 zipcode_l.grid(row=5,column=0)
 
 
 for record in record:
  f_name_e.insert(0,record[0])
  l_name_e.insert(0,record[1])
  address_e.insert(0,record[2])
  city_e.insert(0,record[3])
  state_e.insert(0,record[4])
  zipcode_e.insert(0,record[5])
 
 
 
 sa_b=Button(editor,text="Save Records",command=update)
 sa_b.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
 
     #commit changes
 conn.commit()

     #closed connection
 conn.close()
 
  
def delete():
 conn=sqlite3.connect('address_book.db')

  # create cursor
 c=conn.cursor()

 
 
 
 
 c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
 
 
 
 
 
 
 
 
 
 
 

       #commit changes
 conn.commit()

     #closed connection
 conn.close()
  
 
def submit():

   
  conn=sqlite3.connect('address_book.db')
  c=conn.cursor()
  c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
                            
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
                
            }

            )
               
          #commit changes
  conn.commit()

     #closed connection
  conn.close()
  





   
  f_name.delete(0,END)
  l_name.delete(0,END)
  address.delete(0,END)
  city.delete(0,END)
  state.delete(0,END)
  zipcode.delete(0,END)



def query():
 conn=sqlite3.connect('address_book.db')

  # create cursor
 c=conn.cursor()
 c.execute("SELECT * ,oid FROM addresses")
 record=c.fetchall()
 
 print_record=''
 for record in record:
   print_record+=str(record[6])+" "+str(record[0])+" "+str(record[1])+"\n"
 
 q_l=Label(root,text=print_record)
 q_l.grid(row=12,column=0,columnspan=2)
 
 
 
 
 
 
 
 
   #commit changes
 conn.commit()

  #closed connection
 conn.close()
 
 return


f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))


l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)


address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)


city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)


state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)


zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20)



f_name_l=Label(root,text="First Name")
f_name_l.grid(row=0,column=0,pady=(10,0))
l_name_l=Label(root,text="Last Name")
l_name_l.grid(row=1,column=0)
address_l=Label(root,text="Address")
address_l.grid(row=2,column=0)
city_l=Label(root,text="city")
city_l.grid(row=3,column=0)
state_l=Label(root,text="state")
state_l.grid(row=4,column=0)
zipcode_l=Label(root,text="zipcode")
zipcode_l.grid(row=5,column=0)
delete_box_l=Label(root,text="Select ID")
delete_box_l.grid(row=9,column=0)

sub_b=Button(root,text="Add Data",command=submit)
sub_b.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=130)

q_b=Button(root,text="Show Data",command=query)

q_b.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=130)

   #create a database or coonect to one

del_b=Button(root,text="Delete Records",command=delete)
del_b.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=120)
u_b=Button(root,text="Edit Records",command=edit)
u_b.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=120)
  
    
  
  #commit changes
conn.commit()

  #closed connection
conn.close()
root.mainloop()