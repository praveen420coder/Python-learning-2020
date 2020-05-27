from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("600x100")

def zipLookup():

 try:

  api_req=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip1.get() + "&distance=25&API_KEY=3A66D1A0-A6BB-4D91-8CE5-B20173E151C3")
 

  api=json.loads(api_req.content)
  city = api[0]['ReportingArea']
  quality=api[0]['AQI']
  category=api[0]['Category']['Name']
  if category == "Good":
   w_c="#0C0"
  elif category == "Moderate":
   w_c="#FFFF00"
  elif category == "Unhealthy for Sensitive Groups":
   w_c="#ff9900"
  elif category == "Unhealthy":
   w_c="#FF0000"
  elif category == "Very Unhealthy":
   w_c="#990066"
  elif category == "Hazardous":
   w_c="#660000"
 
 
  mylabel=Label(root,text=city + "  Air Quality : " + str(quality) +" "+category,font=("Helvetica",15),background=w_c)
  mylabel.grid(row=1,column=0,columnspan=2)
  root.configure(background=w_c)
 except Exception as e:
  api="ERROR...."
  

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=3A66D1A0-A6BB-4D91-8CE5-B20173E151C3


zip1=Entry(root)
zip1.grid(row=0,column=0,stick=W+E+N+S)

zipButton=Button(root,text="Lookup ZipCode",command=zipLookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S)







root.mainloop()