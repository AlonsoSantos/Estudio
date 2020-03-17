# RADIO BUTTON
from tkinter import *
raiz = Tk()

opcion=IntVar()

def imprimir():
    if opcion.get() == 1:
        etiqueta.config(text='Has elegido masculino')
    else:
        etiqueta.config(text='Has elegido femenino')

Label(raiz, text='Seleccione su género:').pack()
Radiobutton(raiz,text='Masculino', variable=opcion, value=1, command=imprimir).pack()
Radiobutton(raiz,text='Femenino', variable=opcion, value=2, command=imprimir).pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()