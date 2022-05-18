from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.resizable(False,False)
e=Entry(root,borderwidth=2,width=45)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click_button(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number=e.get()
	global fnum 
	global f
	f='add'
	fnum=int(first_number)
	e.delete(0,END)

def button_equal():
	second_number =e.get()
	e.delete(0,END)
	if f=='add':
		e.insert(0,fnum+int(second_number))
	if f=='sub':
	    e.insert(0,fnum-int(second_number))
	if f=='mul':
	    e.insert(0,fnum*int(second_number))
	if f=='div':
		try:
			e.insert(0,fnum/int(second_number))
		except ZeroDivisionError:
			e.insert(0,'~')
def button_sub():
	first_number=e.get()
	global fnum 
	global f
	f='sub'
	fnum=int(first_number)
	e.delete(0,END)

def button_mul():
	first_number=e.get()
	global fnum 
	global f
	f='mul'
	fnum=int(first_number)
	e.delete(0,END)

def button_div():
	first_number=e.get()
	global fnum 
	global f
	f='div'
	fnum=int(first_number)
	e.delete(0,END)

b=Button(root,text='1',padx=40,pady=20,command=lambda: click_button(1)).grid(row=3,column=0) 
b1=Button(root,text='2',padx=40,pady=20,command=lambda: click_button(2)).grid(row=3,column=1) 
b2=Button(root,text='3',padx=40,pady=20,command=lambda: click_button(3)).grid(row=3,column=2) 
b3=Button(root,text='4',padx=40,pady=20,command=lambda: click_button(4)).grid(row=2,column=0) 
b4=Button(root,text='5',padx=40,pady=20,command=lambda: click_button(5)).grid(row=2,column=1) 
b5=Button(root,text='6',padx=40,pady=20,command=lambda: click_button(6)).grid(row=2,column=2) 
b6=Button(root,text='7',padx=40,pady=20,command=lambda: click_button(7)).grid(row=1,column=0) 
b7=Button(root,text='8',padx=40,pady=20,command=lambda: click_button(8)).grid(row=1,column=1) 
b8=Button(root,text='9',padx=40,pady=20,command=lambda: click_button(9)).grid(row=1,column=2) 
b9=Button(root,text='0',padx=40,pady=20,command=lambda: click_button(0)).grid(row=4,column=0) 
badd=Button(root,text='+',padx=39.25,pady=20,command=button_add).grid(row=4,column=1)
bclear=Button(root,text='Clear',padx=79.25,pady=20,command=button_clear).grid(row=5,column=1,columnspan=2) 
bequal=Button(root,text='=',padx=88.35,pady=20,command=button_equal).grid(row=6,column=1,columnspan=2)
bsub=Button(root,text='-',padx=41,pady=20,command=button_sub).grid(row=4,column=2)
bmul=Button(root,text='*',padx=41,pady=20,command=button_mul).grid(row=5,column=0)
bdiv=Button(root,text='/',padx=41,pady=20,command=button_div).grid(row=6,column=0) 

root.mainloop()