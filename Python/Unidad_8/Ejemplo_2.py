# LABEL
from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
# miLabel = Label(miFrame, text='Hola mundo', fg='red', font=('Comic Sans MS', 18))
# miLabel.place(x=100, y=200)
miImagen = PhotoImage(file='C:/Users/odair/OneDrive/Imágenes/Fondos de pantalla/1012343.png')
# Label(miFrame, text='Hola mundo', fg='red', font=('Comic Sans MS', 18)).place(x=100, y=200) #Simplificado
# Tambien se usa para mostrar imagenes
Label(miFrame, image=miImagen).place(x=100, y=200)

raiz.mainloop()
