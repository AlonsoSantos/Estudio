# INPUT
from tkinter import *
raiz = Tk()

miFrame = Frame(raiz, width=800, height=400)
miFrame.pack()

miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre)
# cuadroTexto.place(x=100,y=100) # Esto es machete
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg='red', justify='center')
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show='*')
nombreLabel = Label(miFrame, text='Nombre: ')
# nombreLabel.place(x=100,y=70) # Esto es machete
# e = este
# n = norte
# s = sur
# w = oeste
# padx es espacio antes y despues del label
# pady es espacio arriba y abajo del label
nombreLabel.grid(row=0, column=0, sticky='w', padx=10, pady=10)
apellidoLabel = Label(miFrame, text='Apellido: ')
apellidoLabel.grid(row=1, column=0, sticky='w', padx=10, pady=10)
direccionLabel = Label(miFrame, text='Dirección: ')
direccionLabel.grid(row=2, column=0, sticky='w', padx=10, pady=10)
passLabel = Label(miFrame, text='Password: ')
passLabel.grid(row=3, column=0, sticky='w', padx=10, pady=10)


def codigoBoton():
    miNombre.set('Alonso')


# BUTTON
botonEnvio = Button(raiz, text='Enviar', command=codigoBoton)
botonEnvio.pack()

# TEXT
cuadroComentario = Text(miFrame, width=15, height=5)
cuadroComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=cuadroComentario.yview)
# sticky='nsew' posiciona al scroll al lado del cuadro de texto de comentarios del mismo tamaño que el cuadro de texto
scrollVertical.grid(row=4, column=2, sticky='nsew')
cuadroComentario.config(yscrollcommand=scrollVertical.set)
comentarioLabel = Label(miFrame, text='Comentario: ')
comentarioLabel.grid(row=4, column=0, sticky='w', padx=10, pady=10)

raiz.mainloop()
