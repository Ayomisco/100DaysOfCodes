from tkinter import *
from tkinter import filedialog, ttk

from pytube import YouTube
from tkinter.ttk import *

window = Tk()
window.geometry("500x500+350+100")
window.title("YouTube Downloader")
window.resizable(False, False)
window.config(bg="gray3")

# Global Variable
direct = ""


# Functions to be Executed
def open_path():
    download_out.config(text="Just be calm and wait if system show No Responding",
                        font=("Bahnschrift SemiBold", 10, "bold"))
    download_name.config(text="")
    download_size.config(text="")
    download_loc.config(text="")
    global direct
    direct = filedialog.askdirectory()
    path_holder.config(text=direct)

def Download():
    url = link_entry.get()
    selected = types.get()

    if len(url) < 1:
        link_error.config(text="Please insert a URL")
    if len(direct) < 1:
        path_error.config(text="Please Insert a Location path")
    else:
        link_error.config(text="")
        path_error.config(text="")
        try:
            yt = YouTube(url)
            try:
                if selected == options[0]:
                    typ = yt.streams.get_highest_resolution()

                elif selected == options[1]:
                    typ = yt.streams.filter(progressive=True, file_extension="mp4").first()

                elif selected == options[2]:
                    typ = yt.streams.filter(only_audio=True).first()

                try:
                    typ.download(direct)
                    link_entry.delete(0, "end")
                    path_holder.config(text="\t\t\t\t      ")
                    download_out.config(text="Downloaded", font=(12))

                    name = typ.title
                    size = typ.filesize / 1024000
                    size = round(size, 1)
                    download_name.config(text="Name : " + name)
                    download_size.config(text="Size : " + str(size) + "MB")
                    download_loc.config(text="PATH :" + direct)

                except:
                    download_out.config(text="Download Failed", font=12)
            except:
                download_out.config(text="Having Error", font=(12))
        except:
            path_error.config(text="Please insert a valid path")


# Functions to be executed Ends


# Heading Start Here
heading = Label(window, text="YouTube Video Downloader", background="grey3", foreground="dark orange",
                font=("Bahnschrift SemiBold", 20, "bold"))
heading.pack(anchor="center", pady=10)  # Centralised the heading
# Heading Ends Here

# Youtube URL to be enter
link = Label(window, text="Url", background="grey3", foreground="dark orange",
             font=("Bahnschrift SemiBold", 10))
link.pack(anchor="nw", padx=30, pady=25)  # Centralised the Link
entry_url = StringVar()
link_entry = Entry(window, width=52, textvariable=entry_url)  # For the Input
link_entry.place(x=90, y=83)
# Youtube URL to be enter Ends Here
# LINK ERROR
link_error = Label(window, text="Demo", background="grey3", foreground="dark orange",
                   font=("Bahnschrift SemiBold", 10))
link_error.place(x=300, y=105)

# Folder Path Begins
path = Label(window, text="Path", background="grey3", foreground="dark orange",
             font=("Bahnschrift SemiBold", 10))
path.pack(anchor="nw", padx=30, pady=2)  # Centralised the Link

path_holder = Label(window, text="\t\t\t\t", background="white", foreground="black",
                    font=("Bahnschrift SemiBold", 10))
path_holder.place(x=92, y=130)

# Path style ###
path_style = ttk.Style()
path_style.configure("PT.TButton", background="DarkOrange1", foreground="DarkOrange1",
                     font=("Bahnschrift SemiBold", 10))

# Path Button
path_btn = Button(window, width=11, text="Select Path", style="PT.TButton", command=open_path)

path_btn.place(x=323, y=125)

# Path Error
path_error = Label(window, text="Demo", background="grey3", foreground="dark orange",
                   font=("Bahnschrift SemiBold", 10))
path_error.place(x=300, y=155)

# Folder Path Ends here

# Download Quality Type Starts
download_type = Label(window, text="Download Quality", background="grey3", foreground="dark orange",
                      font=("Bahnschrift SemiBold", 10))
download_type.pack(anchor="w", padx=30, pady=25)

options = ['High Quality', "Low Quality", "Audio"]

types = ttk.Combobox(window, values=options, width=23)
types.current(0)
types.place(x=140, y=175)

choose_type = Label(window, text="Choose type", background="grey3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
choose_type.place(x=315, y=175)

# Download Quality Type Ends

# Download Button Starts
download_style = ttk.Style()
download_style.configure("DO.TButton", background="DarkOrange1", foreground="DarkOrange1",
                         font=("Bahnschrift SemiBold", 10))

download_btn = Button(window, width=40, text="Download", style="PT.TButton", command=Download)
download_btn.pack(anchor="center", pady=30)

# Patience While Downloading
download_out = Label(window, text="Wait if system show No Responding during Download", background="grey3",
                     foreground="dark orange",
                     font=("Bahnschrift SemiBold", 10))
download_out.pack(anchor="center", pady=10)

# Video Name
download_name = Label(window, background="grey3", foreground="dark orange",
                      font=("Bahnschrift SemiBold", 10))
download_name.pack(anchor="nw", padx=30, pady=10)

# File Size
download_size = Label(window, background="grey3", foreground="dark orange",
                      font=("Bahnschrift SemiBold", 10))
download_size.pack(anchor="nw", padx=30, pady=10)

# File lOcation Display
download_loc = Label(window, background="grey3", foreground="dark orange",
                     font=("Bahnschrift SemiBold", 10))
download_loc.pack(anchor="nw", padx=30, pady=10)
# Download Button Ends

# copyright name
copyright_detail = Label(window, text="OGTConsult @ Ayomisco", background="grey3", foreground="dark orange",
                         font=("Bahnschrift SemiBold", 10))
copyright_detail.pack(anchor="center", padx=30)
copyright_detail.place(x=180, y=370)
# Download Button Ends


mainloop()
