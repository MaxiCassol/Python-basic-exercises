import tkinter
from tkinter import ttk

window = tkinter.Tk()

def reinicio(event):
    print("Reinicio")
    seleccionado.set(None)


window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='opcion 1', value='1', variable=seleccionado) #variable los agrupa juntos
r2 = ttk.Radiobutton(window, text='opcion 2', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='opcion 3', value='3', variable=seleccionado)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

botonReinicio = tkinter.Button(window, text='Reiniciar')
botonReinicio.grid(column=1, row=4, pady=5, padx=5)
botonReinicio.bind('<Button-1>', reinicio)



window.mainloop()
