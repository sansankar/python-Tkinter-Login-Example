
from tkinter import *
import tkinter.messagebox
import sqlite3
# from PIL import ImageTk, Image

root = Tk()
root.title ("Login Python Example")
root.geometry ("350x150+500+250")

labelframe = LabelFrame(root,background="pink", text="Login")

labelframe.pack(fill="both", expand="yes")

Label(labelframe, text = "UserName:").grid(row=3,column=0,sticky=W+E+N+S,padx=5, pady=5)
user1 = Entry(labelframe)
user1.grid(row=3,column=1,sticky=W+E+N+S,padx=5, pady=5)



Label(labelframe, text = "Password:").grid(row=4,column=0,sticky=W+E+N+S,padx=5, pady=5)
uspass = Entry(labelframe, show = "*")
uspass.grid(row=4,column=1,sticky=W+E+N+S,padx=5, pady=5)


# img = ImageTk.PhotoImage(Image.open("batman.jpg"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")

def login():
	# Connect to database
	db = sqlite3.connect('D:/python/python/Login-con-Tkinter-y-Python-master/login.db')
	c = db.cursor()
	
	user = user1.get()
	paswd = uspass.get()


	
	c.execute('SELECT * FROM users WHERE   user = ? AND pass = ?', (user, paswd))
	r=c.fetchall()
	for row in r:
		if r!=0:
			tkinter.messagebox.showinfo(title = "Login correct", message = "Login Successs")
			break
	else:
		tkinter.messagebox.showerror(title = "Login incorrect", message = "User Name or Password Incorrect")
		
	c.close()

Button (labelframe,text = "Login", command = login).grid(row=5,column=2,padx=10,pady=2)


root.mainloop()
