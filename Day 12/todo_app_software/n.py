
from tkinter import *

#declare gui object and classes
app = Tk() #creates instance of Tk()
app.title('Check sort DCA') # sets title of gui
#---------------------------------------
def keepSuggested(): #button press actions 
    es.JournalOut('test2')
def UseNew():
    es.JournalOut('test1')
#------------------------------
frame=Frame(app,width=500,height=500)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=500,height=500,scrollregion=(0,0,500,500))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=500,height=500)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(expand=True,fill=BOTH)


spacer1 = Label(canvas, text='|')
spacer2 = Label(canvas, text='|')
spacer3 = Label(canvas, text='|')
spacer4 = Label(canvas, text='|')
spacer5 = Label(canvas, text='|')

Chan_Num = Label(canvas,text='Channel Number')
Chan_Name = Label(canvas, text='Channel Name')
NewChan_Num = Label(canvas, text='New Channel Number')
Set_Title = Label(canvas, text='Set New')
std_Num=Label(canvas, text='Standard Channel Number')
std_Name = Label(canvas, text='Standard Channel Name')

Chan_Num.grid(row=0, column=0)
spacer1.grid(row=0, column=1)
Chan_Name.grid(row=0, column=2)
spacer2.grid(row=0, column=3)
NewChan_Num.grid(row=0, column=4)
spacer3.grid(row=0, column=5)
Set_Title.grid(row=0, column=6)
spacer4.grid(row=0,column=7)
std_Num.grid(row=0,column=8)
spacer5.grid(row=0,column=9)
std_Name.grid(row=0,column=10)



n=0
i = 0 # loops through all channel numbers to get print table value.
while i < nchan:  # prints out all present channels with index and channel number and title #populates tables
    ch_name = tsin.GetChanTitle(i)
    ch_num = tsin.GetChanNumber(i)


    ch_name_list = Label(canvas, text=ch_name )
    ch_num_list = Label(canvas, text=str(ch_num))



    ch_name_list.grid(row=i + 1, column=2)
    ch_num_list.grid(row=i + 1, column=0)
    UserInput=StringVar()
    EntryBox= Entry(canvas, textvariable = UserInput)
    EntryBox.grid(row=i+1,column=4 )




    i = i + 1
j=0
while j< len(CorrectChannels):
    stdList= CorrectChannels[j]
    stdListNum = j
    std_ch_num= Label(canvas,text=stdListNum+1) 
    std_ch_name = Label(canvas,text=stdList)
    std_ch_name.grid(row=j+1, column=10)
    std_ch_num.grid(row=j+1, column=8)
    j=j+1 
#build gui elements
Buttonnew = Button(canvas, text='Set Channels', bg='blue', fg='white',command=UseNew)
Buttonnew.grid(row=1, column=6)
Buttonkeep = Button(canvas, text='keep channels', bg='blue', fg='white', command=keepSuggested)
Buttonkeep.grid(row=2, column=6)




app.mainloop()