from tkinter import *

# Function for clicking the buttons
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


# Clear Button Function Display
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


# Equal Button Function Display
def equalBtnInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
# Cal Title
cal.title("Calculator by Ayomisco")
operator = ""

# This is for the number input
text_Input = StringVar()

txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg='powder blue',justify='right' ).grid(columnspan=4) # Grid columnspan is responsible for the outlook of the 

# Button for the Input Number row 1
btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", command=lambda:btnClick(7), bg='powder blue').grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg='powder blue', command=lambda: btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg='powder blue', command=lambda: btnClick(9)).grid(row=1, column=2)
            
additionbtn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="+", bg='powder blue', command=lambda: btnClick("+")).grid(row=1, column=3)


# =======================Button for the Input Number row 2
btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg='powder blue', command=lambda: btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg='powder blue', command=lambda: btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg='powder blue', command=lambda: btnClick(6)).grid(row=2, column=2)

subtractionbtn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                        text="-", bg='powder blue', command=lambda: btnClick("-")).grid(row=2, column=3)


# =======================Button for the Input Number row 2
btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg='powder blue', command=lambda: btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg='powder blue', command=lambda: btnClick(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg='powder blue', command=lambda: btnClick(3)).grid(row=3, column=2)

multiplybtn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="*", bg='powder blue', command=lambda: btnClick("*")).grid(row=3, column=3)


# =======================Button for the Input Number row 2
btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg='powder blue', command=lambda: btnClick(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="c", bg='powder blue', command=btnClearDisplay).grid(row=4, column=1)

equalBtn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="=", bg='powder blue', command=equalBtnInput).grid(row=4, column=2)

divisionBtn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="/", bg='powder blue', command=lambda: btnClick("/")).grid(row=4, column=3)





cal.mainloop()
