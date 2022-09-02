# from cgitb import text
from tkinter import *
import random
import ttkthemes
# Applying
from tkinter import ttk
from time import sleep
# Calling the tkinter environmment

# Using threading to allow two function to be executed at the same time
import threading

################### fUNCTION PART
total_time = 60
time = 0
wrong_words = 0
elapse_time_in_minute = 0
def start_timer():
        start_button.config(state=DISABLED)
        global time
        # Selecting textarea tonormal on start click
        textarea.config(state=NORMAL)
        #  Making pointer to appear automatically
        textarea.focus()


        for time in range(1, 61):
                used_time_label.config(text=time)
                remaining_time = total_time - time
                remaining_time_label.config(text=remaining_time)
                sleep(1)
                root.update()

        textarea.config(state=DISABLED)
        reset_button.config(state=NORMAL)




# Counting words function
def count():
        global wrong_words
        while time != total_time:
                entered_paragraph = textarea.get(1.0, END).split()
                total_words = len(entered_paragraph)
        
        total_words_count_label.config(text=total_words)

        #  Comparing and getting wrong words
        paragraph_word_list = paragraph_label["text"].split()

        # getting and zipping each word in a turple
        for pair in list(zip(paragraph_word_list, entered_paragraph)):
                if pair[0] != pair[1]:
                        wrong_words += 1

        
        wrong_words_count_label.config(text=wrong_words)

        elapse_time_in_minute = time/60
        wpm = (total_words - wrong_words) / elapse_time_in_minute
        wpm_count_label.config(text=wpm)

        # Checking how many words you are typing by minutes
        gross_wpm = total_words/elapse_time_in_minute
        accuracy = wpm/gross_wpm * 100
        accuracy = round(accuracy)
        accuracy_percentage_label.config(text=str(accuracy)+'%')

def start():
        t1 = threading.Thread(target=start_timer)
        t1.start()

        t2 = threading.Thread(target=count)
        t2.start()




def reset():
        global time, elapse_time_in_minute
        time = 0
        start_button.config(state=NORMAL)
        reset_button.config(state=DISABLED)
        textarea.config(state=NORMAL)

        # TEXT
        textarea.delete(1.0, END)
        textarea.config(state=DISABLED)

        used_time_label.config(text='0')
        remaining_time_label.config(text='0')
        wpm_count_label.config(text='0')
        accuracy_percentage_label.config(text='0')
        total_words_count_label.config(text='0')
        wrong_words_count_label.config(text='0')
        used_time_label.config(text='0')

################ GUI PART ########################### 
# Calling theme
# We used ThemeTk instaead of Tk()
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
# Removing the Top Menu
root.overrideredirect(True)

# Declaring the geometry or the size of the window and also declared the position of the window
root.geometry("940x735+200+35")
root.resizable(0,0)


mainFrame = Frame(root,bd=4)
mainFrame.grid()

# Title Frame
titleFrame = Frame(mainFrame, bg="#f1ce32")
titleFrame.grid(row=0, column=0)

#Title Label
title_label = Label(titleFrame, text="Master Typing", font=("algerian", 28, "bold" ), 
                bg="#d8b416", fg="white",width=38, bd=10)
title_label.pack(pady=5)

# Paragraph Frame
paragraph_frame = Frame(mainFrame)
paragraph_frame.grid(row=1, column=0)

#Paragraph Label
paragraph_list = ['Railway is a deployment platform where you can provision infrastructure, develop with that infrastructure locally, and then deploy to the cloud.',
                    'First, to deploy the NextJS Prisma starter, we will make a new project.Railway offers a Command Palette that exposes all actions that one can do on the platform. We will use this menu to create our project.Press the Command + K key combination and type \"New Project".',
                    'Here\'s another gentle nudge to remind you of your class today at 09:00 pm (IST) on Dare to Dream.You can login to scaler.com and join through the option on the dashboard.',
                    'Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being',
                    'Extra tartalmakért kövess be Instán: https://bit.ly/38hVdUE Itt tolom a liveokat, Trovo: https://trovo.live/KDS Discord szerverem: https://discord.gg/x4UnxkASBu KDShorts csatorna: … ']

# Shuffling the paragraoh List
random.shuffle(paragraph_list)

#wrap length wrap the text to fit in the text
paragraph_label = Label(paragraph_frame, text=paragraph_list[0], wraplength=912,
        justify='left', font=('arial', 14,'bold'))
paragraph_label.grid(row=0,column=0, pady=9)

# tEXT AREA FRAME
textarea_frame =  Frame(mainFrame)
textarea_frame.grid(row=2, column=0)

# textarea Label Textarea
textarea = Text(textarea_frame, font=('arial', 12, 'bold'), height=7, width=100,wrap=WORD,
            relief=GROOVE, state=DISABLED )
            
textarea.grid()

output_frame = Frame(mainFrame)
output_frame.grid(row=3, column=0)

# Elapse Time
used_time_label = Label(output_frame, text="Used Time: ", font=('Tahoma', 12, 'bold'),
                fg='red')
used_time_label.grid(row=0, column=0)

used_time_label = Label(output_frame, text="0", font=('Tahoma', 12, 'bold'),
                fg='black')
used_time_label.grid(row=0, column=1, padx=8)

# Timer
remaining_time_label = Label(output_frame, text="Remaining Time:", font=('Tahoma', 12, 'bold'),
                fg='red')
remaining_time_label.grid(row=0, column=2)

remaining_time_label = Label(output_frame, text="60", font=('Tahoma', 12, 'bold'),
                fg='black')
remaining_time_label.grid(row=0, column=3, padx=8)

# Timer
wpm_label = Label(output_frame, text="WPM:", font=('Tahoma', 12, 'bold'),
                fg='red')
wpm_label.grid(row=0, column=4)

wpm_count_label = Label(output_frame, text="0", font=('Tahoma', 12, 'bold'),
                fg='black')
wpm_count_label.grid(row=0, column=5, padx=8)

# Accuracy
accuracy_label = Label(output_frame, text="Acuracy:", font=('Tahoma', 12, 'bold'),
                fg='red')
accuracy_label.grid(row=0, column=6)

accuracy_percentage_label = Label(output_frame, text="0", font=('Tahoma', 12, 'bold'),
                fg='black')
accuracy_percentage_label.grid(row=0, column=7, padx=8)

# Total WORDS
total_words_label = Label(output_frame, text="Total Words:", font=('Tahoma', 12, 'bold'),
                fg='red')
total_words_label.grid(row=0, column=8)

total_words_count_label = Label(output_frame, text="0", font=('Tahoma', 12, 'bold'),
                fg='black')
total_words_count_label.grid(row=0, column=9, padx=8)


# Wrong words
wrong_words_label = Label(output_frame, text="Wrong Words:", font=('Tahoma', 12, 'bold'),
                fg='red')
wrong_words_label.grid(row=0, column=10)

wrong_words_count_label = Label(output_frame, text="0", font=('Tahoma', 12, 'bold'),
                fg='black')
wrong_words_count_label.grid(row=0, column=11)


# Options Frame
button_frames = Frame(mainFrame)
button_frames.grid(row=4,column=0)

#start button
start_button = ttk.Button(button_frames, text="Start",  command=start )
start_button.grid(row=0, column=0, padx=10)

#Reset button
reset_button = ttk.Button(button_frames, text="Reset", state='disabled', command=reset)
reset_button.grid(row=0, column=1, padx=10)

#Exit button
exit_button = ttk.Button(button_frames, text="Exit App", command=root.destroy )
exit_button.grid(row=0, column=2, padx=10)

# Keyboard Label
keyboard_frame = Frame(mainFrame)
keyboard_frame.grid(row=5, column=0 , pady=5)

frame_1_to_0 = Frame(keyboard_frame)
frame_1_to_0.grid(row=0, column=0)

# Label 1
label_1 = Label(frame_1_to_0, text="1",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 2
label_2 = Label(frame_1_to_0, text="2",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 3
label_3 = Label(frame_1_to_0, text="3",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 4
label_4 = Label(frame_1_to_0, text="4",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 5
label_5 = Label(frame_1_to_0, text="5",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 6
label_6 = Label(frame_1_to_0, text="6",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 7
label_7 = Label(frame_1_to_0, text="7",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 8
label_8 = Label(frame_1_to_0, text="8",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 9
label_9 = Label(frame_1_to_0, text="9",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
# Label 0
label_0 = Label(frame_1_to_0, text="0",fg="white", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)

label_1.grid(row=0, column=0, padx=5)
label_2.grid(row=0, column=1, padx=5)
label_3.grid(row=0, column=2, padx=5)
label_4.grid(row=0, column=3, padx=5)
label_5.grid(row=0, column=4, padx=5)
label_6.grid(row=0, column=5, padx=5)
label_7.grid(row=0, column=6, padx=5)
label_8.grid(row=0, column=7, padx=5)
label_9.grid(row=0, column=8, padx=5)
label_0.grid(row=0, column=9, padx=5)

frame_q_to_p = Frame(keyboard_frame)
frame_q_to_p.grid(row=1, column=0, pady=10)

label_q = Label(frame_q_to_p, fg="white", text="Q", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_w = Label(frame_q_to_p, fg="white", text="W", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_e = Label(frame_q_to_p, fg="white", text="E", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_r = Label(frame_q_to_p, fg="white", text="R", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_t = Label(frame_q_to_p, fg="white", text="T", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_y = Label(frame_q_to_p, fg="white", text="Y", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_u = Label(frame_q_to_p, fg="white", text="U", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_i = Label(frame_q_to_p, fg="white", text="I", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_o = Label(frame_q_to_p, fg="white", text="O", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_p = Label(frame_q_to_p, fg="white", text="P", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)


label_q.grid(row=0, column=0, padx=5)
label_w.grid(row=0, column=1, padx=5)
label_e.grid(row=0, column=2, padx=5)
label_r.grid(row=0, column=3, padx=5)
label_t.grid(row=0, column=4, padx=5)
label_y.grid(row=0, column=5, padx=5)
label_u.grid(row=0, column=6, padx=5)
label_i.grid(row=0, column=7, padx=5)
label_o.grid(row=0, column=8, padx=5)
label_p.grid(row=0, column=9, padx=5)

# A - L
frame_a_to_l = Frame(keyboard_frame)
frame_a_to_l.grid(row=2, column=0)

label_a = Label(frame_a_to_l, fg="white", text="A", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_s = Label(frame_a_to_l, fg="white", text="S", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_d = Label(frame_a_to_l, fg="white", text="D", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_f = Label(frame_a_to_l, fg="white", text="F", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_g = Label(frame_a_to_l, fg="white", text="G", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_h = Label(frame_a_to_l, fg="white", text="H", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_j = Label(frame_a_to_l, fg="white", text="J", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_k = Label(frame_a_to_l, fg="white", text="K", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_l = Label(frame_a_to_l, fg="white", text="L", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)

label_a.grid(row=0, column=0, padx=5)
label_s.grid(row=0, column=1, padx=5)
label_d.grid(row=0, column=2, padx=5)
label_f.grid(row=0, column=3, padx=5)
label_g.grid(row=0, column=4, padx=5)
label_h.grid(row=0, column=5, padx=5)
label_j.grid(row=0, column=6, padx=5)
label_k.grid(row=0, column=7, padx=5)
label_l.grid(row=0, column=8, padx=5)

# Z - M
frame_z_to_m = Frame(keyboard_frame)
frame_z_to_m.grid(row=3, column=0, pady=10)

label_z = Label(frame_z_to_m, fg="white", text="Z", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_x = Label(frame_z_to_m, fg="white", text="X", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_c = Label(frame_z_to_m, fg="white", text="C", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_v = Label(frame_z_to_m, fg="white", text="V", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_b = Label(frame_z_to_m, fg="white", text="B", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_n = Label(frame_z_to_m, fg="white", text="N", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_m = Label(frame_z_to_m, fg="white", text="M", bg='black', font=('arial', 12, 'bold'), width=5, height=2, bd=10, relief=GROOVE)

label_z.grid(row=0, column=0, padx=5)
label_x.grid(row=0, column=1, padx=5)
label_c.grid(row=0, column=2, padx=5)
label_v.grid(row=0, column=3, padx=5)
label_b.grid(row=0, column=4, padx=5)
label_n.grid(row=0, column=5, padx=5)
label_m.grid(row=0, column=6, padx=5)

# SPACE
space_frame = Frame(keyboard_frame)
space_frame.grid(row=4, column=0)

label_space = Label(space_frame, fg="white", text="", bg='black', font=('arial', 12, 'bold'), width=40, height=2, bd=10, relief=GROOVE)

label_space.grid(row=0, column=0,)


#Function to change background on click
def change_bg(widget):
         widget.config(bg='blue')
         widget.after(600, lambda : widget.config(bg="black"))


# LIST FOR THR KEYS 
number_label_list = [
        label_0, label_1, label_2, label_3, label_4, label_5,label_6, label_7, label_8, label_9, label_0
]       

alphabets_label_list = [
        label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h,
        label_i,label_j, label_k, label_l, label_m, label_n, label_o, label_p, label_q,
        label_r, label_s, label_t, label_u, label_v, label_w, label_x, label_y, label_z
]

space_label_list = [label_space]

binding_number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

binding_upper_case_alphabet_list = [
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]

binding_lower_case_alphabet_list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 'l', 'm', "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]

# binding numbers
for numbers in range(len(binding_number_list)):
        root.bind(binding_number_list[numbers], lambda event, label=number_label_list[numbers]: change_bg(label))

# print(len(alphabets_label_list))
# print(len(binding_upper_case_alphabet_list))


# Binding Alphabets
#  Upper Case
for capital_alphabets in range(len(binding_upper_case_alphabet_list)):
        root.bind(binding_upper_case_alphabet_list[capital_alphabets], lambda event, label= alphabets_label_list[capital_alphabets]: change_bg(label))

for lower_alphabets in range(len(binding_lower_case_alphabet_list)):
        root.bind(binding_lower_case_alphabet_list[lower_alphabets], lambda event, label= alphabets_label_list[lower_alphabets]: change_bg(label))

# bINDING SPACE BAR
root.bind('<space>', lambda event: change_bg(space_label_list[0]))



root.mainloop()