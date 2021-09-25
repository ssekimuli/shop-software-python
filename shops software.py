from tkinter import *


window=Tk()
window.title('ANDESOFT')
window.geometry('820x500')


sideframe=Frame(window,bg='#1e509a', width=500,height=700)
sideframe.place(y=70)
mg=PhotoImage()
sto=Button(window,text='Add stock',width='20',bg='#008dfa',fg='white')
sto.grid(row=1, column=0)
#side bar menu
stock=Button(sideframe,text='Add stock',width='20',bg='#008dfa',fg='white')
stock.grid(row=1, column=0)
payment=Button(sideframe,text='Payment',width='20',bg='#ababab',fg='#1e509a')
payment.grid(row=2, column=0)
report=Button(sideframe,text='Report',width='20',bg='#ababab',fg='#1e509a')
report.grid(row=3, column=0)
notify=Button(sideframe,text='Notify',width='20',bg='#ababab',fg='#1e509a')
notify.grid(row=4, column=0)
cred=Button(sideframe,text='Creditor',width='20',bg='#ababab',fg='#1e509a')
cred.grid(row=5, column=0)
dem=Button(sideframe,text='Demand',width='20',bg='#ababab',fg='#1e509a')
dem.grid(row=6, column=0)
purc=Button(sideframe,text='Purchase',width='20',bg='#ababab',fg='#1e509a')
purc.grid(row=7, column=0)
staf=Button(sideframe,text='Staff',width='20',bg='#ababab',fg='#1e509a')
staf.grid(row=8, column=0)
sal=Button(sideframe,text='Sales',width='20',bg='#ababab',fg='#1e509a')
sal.grid(row=9, column=0)
pl=Button(sideframe,text='Profit & Loss',width='20',bg='#ababab',fg='#1e509a')
pl.grid(row=10, column=0)

#Top menu
home=Button(window,text='Home',width='10',bg='#1e509a',fg='white')
home.place(x=160,y=20)
service=Button(window,text='In-service',width='10',bg='#1e509a',fg='white')
service.place(x=240,y=20)
paying=Button(window,text='Paying',width='10',bg='#1e509a',fg='white')
paying.place(x=319.5,y=20)
demand=Button(window,text='Demand',width='10',bg='#1e509a',fg='white')
demand.place(x=400,y=20)
none1=Label(window,)
none1.place(x=580,y=20)
srh=Entry(window, width=20,bg='#cccccc',fg='#048aed')
srchl=Button(window,text='SEARCH',bg='#048aed',fg='white')
srchl.place(x=650,y=20)
srh.place(x=525,y=24)
log=Button(window,text='Logout',bg='orange')
log.place(x=740,y=20)

#treeview
tv=Frame(window,bg='#1e509a',width=655,height=420)
tv.place(x=158, y=50)

bottomf=Frame(window,bg='#1e509a')
bottomf.grid(row=15, column=0)



window.mainloop()
