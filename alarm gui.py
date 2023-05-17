from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("Alarm")
root.geometry("550x350")
root.minsize(550,350)
root.maxsize(550,350)

#set a background color
root.configure(bg="#49F")



mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('tone.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(root)
header.place(x=5,y=5)

head =Label(root,text="ALARM CLOCK",font=('comic sans',20),
			bg="light green",fg="black")
head.pack(fill=X)

panel = Frame(root)
panel.place(x=25,y=70)
#panel.configure(bg="#49F")
alpp = PhotoImage(file='al.png')

alp = Label(panel,image=alpp)
alp.grid(rowspan=5,column=4)


atime = Label(panel,text="Alarm Time \n(Hr:Min)",font=('poppins',15))
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('comic sans',20),width=5)
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Message",font=('poppins',18))
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


start = Button(panel,text="Start alarm",font=('poppins',15,"bold"),
			   bg="#50C878",fg="white",command=th)
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)





root.mainloop()