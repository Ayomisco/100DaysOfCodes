from tkinter import *

# Defining window Interface
root = Tk()
root.title("Optimum To-DO App")
root.iconbitmap("check.ico")
root.geometry("420x420")
# root.resizable(0,0)


#defining fonts and color.
my_font = ("Times New Roman", 12)
root_color = "blue"
button_color = "orange"

root.config(bg=root_color)

#Define functions
def add_item():
    """Add an individual item to the listbox"""
    check = u"\u2705 "
    my_listbox.insert(END,check + list_entry.get())
    list_entry.delete(0, END)


def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)

def clear_list():
    """Delete all items from the listbox"""
    my_listbox.delete(0, END)

def save_list():
    """Save the list to a simple txt file"""
    with open('checklist.txt', 'w') as f:
        #listbox.get() returns a tuple....
        list_tuple = my_listbox.get(0, END)
        for item in list_tuple:
            #Take proper precautions to include only one \n for formatting purposes
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + "\n")

def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
             my_listbox.insert(END, line)
    except:
        return


# Main Coding Starts Here
# Defining Layout and Creating Frames
input_frame = Frame(root, bg=root_color)
output_frame = Frame(root, bg=root_color)
button_frame = Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()

button_frame.pack()


# Input frame layout
#Entry box for users to type something on
list_entry = Entry(input_frame, width=37, borderwidth=3, font=my_font)
list_add_button = Button(input_frame, text="Add Item", borderwidth=2,
                    font=my_font, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)



#Output frame layout
my_scrollbar = Scrollbar(output_frame, orient=VERTICAL)
my_listbox = Listbox(output_frame, height=16, width=35, borderwidth=3,
font=('bookman old style', 12, "bold"), yscrollcommand=my_scrollbar.set)
#Link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
# Using sticky property N-North and S-South
my_scrollbar.grid(row=0, column=1, sticky="NS")



#Button Frame layout
list_remove_button = Button(button_frame, text="Remove Item", borderwidth=2,
            font=my_font, bg=button_color)
list_clear_button = Button(button_frame, text='Clear List', borderwidth=2,
            font=my_font, bg=button_color)
save_button = Button(button_frame, text='Save List', borderwidth=2,
            font=my_font, bg=button_color)
quit_button = Button(button_frame, text='Quit', borderwidth=2, font=my_font,
             bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

#Open the previous 

# open_list()
root.mainloop()