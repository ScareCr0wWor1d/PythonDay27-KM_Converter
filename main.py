import tkinter


def buttonclic():
    conv.config(text=round(float(my_input.get())*0.62137, 1))


window = tkinter.Tk()
window.title('KM to Miles Conv.')
window.wm_minsize(200, 150)
window.config(padx=30, pady=30)

my_input = tkinter.Entry(width=10)
my_input.insert(tkinter.END, string='0')
my_input.grid(column=1, row=0)

km = tkinter.Label(text='KM', font=('system', 10))
km.grid(column=2, row=0)

label1 = tkinter.Label(text='is equal to', font=('system', 10))
label1.grid(column=0, row=2)

conv = tkinter.Label(font=('system', 10))
conv.grid(column=1, row=2)

mile = tkinter.Label(text='Miles', font=('system', 10))
mile.grid(column=2, row=2)
mile.config(pady=10)

my_button2 = tkinter.Button(text="Convert", command=buttonclic)
my_button2.grid(column=1, row=4)

window.mainloop()
