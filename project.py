#import libraries which are mandatory for this python code

from Tkinter import *                               #import libarary for gui
import random                                       #generate random
import json                                         #for sending json object
from pymongo import MongoClient                     #database connection
import requests                                     #for data send to server
import time                                         #for delay
import tkMessageBox
import sys                                          #for clear after some time interval
import cookielib                                    #for sms sending
import urllib2                                      #open a url into python terminal
import ttk                                          #for progress bar
import Tkinter as tk
def start_det():
    #create a new window and give progress bar on this
    pro_window=Toplevel()    
    pbar_det = ttk.Progressbar(pro_window, orient="horizontal", length=300, mode="determinate")
  #start_det(pbar_det)
  #pbar_det.grid(row=3, column=0, pady=2, padx=2, sticky=E+W+N+S)
    pbar_det.pack()

    for i in xrange(50):
        pbar_det.step(5)
        pro_window.update()
        # Busy-wait
        time.sleep(0.1)
    pro_window.destroy();





def sms(pno,score):
  #logging into the sms site
   url ='http://site24.way2sms.com/Login1.action?'
   data = 'username='+'7014329137'+'&password='+'F9354D'+'&Submit=Sign+in'

 #For cookies

   cj= cookielib.CookieJar()
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

 #Adding header details
   opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
   try:
       usock =opener.open(url, data)
   except IOError:
       print "error"
        #return()

   jession_id =str(cj).split('~')[1].split(' ')[0]
   send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
   send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+pno+'&message='+'Your score is '+str(score)+'&msgLen=136'
   opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
   try:
       sms_sent_page = opener.open(send_sms_url,send_sms_data)
   except IOError:
       print "error"
        #return()


root =Tk()#create root window
def exit():

   sys.exit()



   #create gui for register which have textbox of username,password,and a button submit
def registerr():
   global E_ru
   global E_rp

   global w3
   w3=Toplevel(root)
   w3.geometry("400x250+200+200")
   L0 = Label(w3, text="REGISTER PAGE",font=15,bg="red")
   L0.pack()
   L1 = Label(w3, text="username",font=15,bg="cyan")
   L1.pack()
   E_ru = Entry(w3, bd =5)
   E_ru.pack()
   L2 = Label(w3, text="password",font=15,bg="cyan")
   L2.pack()
   E_rp= Entry(w3, bd =5)
   E_rp.pack()
   b1=Button(w3,text="Submit",command=register)
   b1.pack()
#check for valid user and send data to the server
def register():

   root.withdraw()
   a=E_ru.get()
   b=E_rp.get()
   MONGODB_URI2 = "mongodb://py:Vmc1234$@ds113136.mlab.com:13136/project"
   #store username and password at mlab
   client2 = MongoClient(MONGODB_URI2, connectTimeoutMS=30000)
   db2 = client2.get_default_database()
   collection3=db2['login']
   db_user2=collection3.find_one({"username":a})
   if (db_user2!=None):
    print "ALready Existing User!"
    tkMessageBox.showinfo("Error","User Already Existing!!!")
    registerr()
   else:


    data1={
            "username":a,
            "password":b
          }
    #post data on server

    links1="https://api.mlab.com/api/1/databases/project/collections/login?apiKey=hN5OWmBavFDkqkD6QCro5EHj426Wrpom"
    r=requests.post(url=links1,json=data1)
    loginn()
#for checking valid user
def check():
  global lu
  global lp
  global lno
  lno=E_no.get()

  lu=E_lu.get()
  lp=E_lp.get()
  MONGODB_URI1 = "mongodb://py:Vmc1234$@ds113136.mlab.com:13136/project"
  client1 = MongoClient(MONGODB_URI1, connectTimeoutMS=30000)                          #it matchs password in database and local password should me match according to user
  db1 = client1.get_default_database()
  collection2=db1['login']
  db_user1=collection2.find_one({"username":lu})
  if(db_user1!=None):
    if(lp==db_user1['password']):
      #print db_user1['password']
      #print lp
      login()
    else:
      print False
  else:
    tkMessageBox.showinfo("Error","Login Unsuccesfull!!!")
    loginn()


#create gui for login which have 3 textbox and a button
def loginn():
   #global w2
   
   global E_lu
   global E_lp
   global E_no

   w2=Toplevel(root)
   w2.geometry("400x250+200+200")
   L0 = Label(w2, text="LOGIN PAGE!",font=15,bg="red")
   L0.pack()
   L1 = Label(w2, text="username",font=15,bg="cyan")
   L1.pack()
   E_lu = Entry(w2, bd =5)
   E_lu.pack()
   L2 = Label(w2, text="password",font=15,bg="cyan")
   L2.pack()
   E_lp = Entry(w2, bd =5)
   E_lp.pack()
   #this is phone number
   #the result of this quiz will send to this number
   L3 = Label(w2, text="Mobile Number",font=15,bg="cyan")
   L3.pack()
   E_no = Entry(w2, bd =5)
   E_no.pack()
   b1=Button(w2,text="Submit",command=check)
   b1.pack()




def on_configure(event):
    
    canvas.configure(scrollregion=canvas.bbox('all'))
#create a frame on window
    #if login is successful
def login():
   root.withdraw()
   #w2.withdraw()
   global user
   global window
   global frame
   global canvas
   #print str(E_lu)
   #print user
   #print type(user)
   user=lu
   
   #create a window and create a frame on it
   window=Toplevel(root)
   window.geometry("1080x800+200+200")
   canvas = Canvas(window)
   canvas.pack(side=LEFT)
   scrollbar = Scrollbar(window, command=canvas.yview)
   scrollbar.pack(side=RIGHT, fill='y')
   canvas.configure(yscrollcommand = scrollbar.set,width=700,height=1000)
   canvas.bind('<Configure>', on_configure)
   frame = Frame(canvas)
   canvas.create_window((0,0), window=frame, anchor='nw')
   L2 = Label(frame, text="Welcome! "+user,font=15,bg="red",anchor="w")
   L2.pack()
#fetch random question from server(mlab)
   
   MONGODB_URI = "mongodb://py:Vmc1234$@ds113136.mlab.com:13136/project"
   client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
   db = client.get_default_database()
   #client.server_info()
   collection=db['quiz']
 #genearate a list  
   k=range(1,16)
#return any 10 number in given range(in this case range is k)
   l=random.sample(k,10)
   global n
   n=0
#fetch  data from mlab
   for i in l:
       temp=collection.find_one({"id":i})
       q=temp["ques"]
       a=temp["a"]
       b=temp["b"]
       c=temp["c"]
       d=temp["d"]
       e=temp["ans"]                                                          #fetch data from server and assign to object then call getdata function of quiz class
       s=temp["sol"]
       obj[n].getdata( q,a,b,c,d,e,s)
       n=n+1
   #button for complete quiz call result function
   b21=Button(frame,text="Submit",command=result)
   b21.pack()
   
   
   
def result():
   window.destroy()
   #call function for craete a progress bar
   start_det()
   new_window=Toplevel(root)
   new_window.geometry("1080x800+200+200")
   i=0
   score=0

   #calculate score of quiz
   while(i<n):
      if(str(obj[i].f)==obj[i].e):
         score=score+1
      
      i=i+1

   L2 = Label(new_window, text="Your score is  "+str(score),font=20,bg="red")
   L2.pack()
   #send data to server 
   data={
          "name":user,
          "score":score
          }
   links="https://api.mlab.com/api/1/databases/project/collections/users?apiKey=hN5OWmBavFDkqkD6QCro5EHj426Wrpom"
   r=requests.post(url=links,json=data)
   #call function for sms sending
   sms(lno,score)



#create a class quiz which have datamember(question and its options) store in string variables
 #create gui of a question
   #which have a question(label) and option (radiobutton)
      
     
class quiz:
    def _init_(self,temp=""):
        self.q=self.a=self.b=self.c=self.d=self.e=self.s=self.f=temp
        
    def select(self):                               #for acknowledgement of which radiobutton is clicked
       self.f=self.var.get()
    def getdata(self,ques,op1,op2,op3,op4,r_op,w_op):
        self.q=ques
        self.a=op1
        self.b=op2
        self.c=op3
        self.d=op4
        self.e=r_op
        self.s=w_op
        self.f="f"
        self.var=IntVar()
        #self.var.set(3)
        L3=(Label(frame, text=self.q, anchor='w',font=20,wraplength=500,justify=LEFT,padx=20).pack(fill='both'))
        R1=Radiobutton(frame,text=self.a,variable=self.var,value=1,command=self.select,font=15,padx=20)
        # R1.select()
        R1.pack(anchor=W)

        
        R2=Radiobutton(frame,text=self.b,variable=self.var,value=2,command=self.select,font=15,padx=20)
         #R2.deselect()
        R2.pack(anchor=W)
         
        R3=Radiobutton(frame,text=self.c,variable=self.var,value=3,command=self.select,font=15,padx=20)
        # R3.deselect()
        R3.pack(anchor=W)
          
        R4=Radiobutton(frame,text=self.d,variable=self.var,value=4,command=self.select,font=15,padx=20)
       #  R4.deselect()
        R4.pack(anchor=W)
        
    
#create list of object of quiz class
global obj
obj=[]
for i in range(100):
  obj.append(quiz())
global w3
global w2
root.geometry("200x100+200+200")
#create label on root window
L1 = Label(root, text="QUIZ MASTER",font=15,bg="cyan")
L1.pack()
#E1 = Entry(root, bd =5)
#E1.pack()
L2 = Label(root, text="")
L2.pack()
#two button for control login and register
b1=Button(root,text="LOGIN",command=loginn)
b1.pack(side=LEFT)
b2=Button(root,text="REGISTER",command=registerr)
b2.pack(side=RIGHT)

#for run a window continuously
root.mainloop()
