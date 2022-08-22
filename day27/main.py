from tkinter import *

FONT=("Arial", 18, "normal")

# def button_clicked():
#     new_text = input.get()
#     label.config(text=new_text)
#     label.grid(column=0, row=0)

# def new_button_click():
#     new_label = Label(text="Yo, Yo, Yolo!", font=FONT)
#     new_label.grid(column=2, row=1)

# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# label = Label(text="I am a label", font=FONT)
# label.grid(column=0, row=0)
# label.config(padx=50, pady=50)

# # Button(s)
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# new_button = Button(text="New Button, Yo", command=new_button_click)
# new_button.grid(column=2, row=0)

# # Entry
# input = Entry(width=10)
# input.grid(column=3, row=2)

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    km_calc.config(text=str(km))
    


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=30, pady=30)


# Entry
input = Entry(width=7)
input.insert(END, "0")
input.grid(column=1, row=0, ipadx=5, ipady=5)
input.focus_set()
# input.config()

# Labels
km_calc = Label(text="0", font=FONT, justify="center")
km_calc.grid(column=1, row=1)

miles_label = Label(text="Miles", font=FONT, justify="left", )
miles_label.grid(column=2, columnspan=2, row=0)
# miles_label.config(pady=20)

eq_label = Label(text="is equal to", font=FONT, justify="right")
eq_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT, justify="center")
km_label.grid(column=2, row=1)


#Button
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2, rowspan=2)
calc_button.config(padx=10)




window.mainloop()

