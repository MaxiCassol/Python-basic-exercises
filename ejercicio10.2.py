from tkinter import *

master = Tk()
elemento = StringVar()

listbox = Listbox(master)
for item in ["Maxi", "Natalia", "Amelia", "Mini", "Lola", "Charly"]: listbox.insert(END, item)
listbox.pack()

label = Label(text="La familia! ")
label.pack()

master.mainloop()