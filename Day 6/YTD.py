from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube  import YouTube 

Folder_Name = ""

# File Location .
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose a Folder!!!", fg="red")

# dOWNLOAD vIDEO
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if len(url) > 1:
        ytdError.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!", fg="red")

    #executing download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")




root = Tk()
root.title("YouTube Downloader") # GUI Title
root.geometry("450x300") # GUI Width
#root.config(bg = 'gray') # Background Color
root.resizable(False,False)
root.iconbitmap('ytd.ico')

root.columnconfigure(0, weight=1) # This set all content in ceter

#YTD Link Label
ytdlabel = Label(root,text="Enter the URL of the video to download", font=("jost",15))
ytdlabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry    = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

# Error Message
ytdError = Label(root, text="Eroor Msg", fg="orange", font=('joot', 10))
ytdError.grid()

# Asking save file label
saveLabel = Label(root, text="Save the video File", font=("jost", 15, "bold"))
saveLabel.grid()

# Button to save file
saveEntry = Button(root, width=10,bg="orange", fg="white", text="Choose Path", command=openLocation)
saveEntry.grid()

# Error Message incase user does not select any Location
locationError = Label(root, text="Path not selected... Pls select path", fg="orange", font=("jost", 10))
locationError.grid()

#Download Quality
ytdQuality = Label(root, text="Select Quality", font=("jost", 15))
ytdQuality.grid()

# (Combobox)Selection Box
choices = ["720p","144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

# Download button
downloadbtn = Button(root, width=10, bg="orange", fg="white", text="Download", command=DownloadVideo)
downloadbtn.grid()

# Dwveloper Label
developerLabel = Label(root, text="OGTConsult @Ayomisco", font=("jost", 15))
developerLabel.grid()


root.mainloop()
