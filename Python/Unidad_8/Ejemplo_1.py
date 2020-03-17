# VENTANA INICIAL
from tkinter import *
raiz = Tk()
# esto establece el titulo de la ventana
raiz.title('Ventana de prueba')
# esto hace que se pueda o que no se pueda arreglar el tamaño de la ventana manualmente resizable(X(Boolean), Y(Boolean))
raiz.resizable(True, True)
# esto es para cambiar el icono de la ventana
raiz.iconbitmap('D:/Estudio/Python/Unidad_8/python_icon.ico')
# esto establece el tamaño de la ventana geometry('XxY')
raiz.geometry('650x350')
# esto establece el color de fondo de la ventana
raiz.config(bg='black')

# FRAME
miFrame = Frame()
# esto empaqueta el frame con la raiz, si se le coloca side dentro de los parentesis es para darle la alineacion
# miFrame.pack(side='left', anchor='n') # n= norte, s = sur, e = este, o = oeste
miFrame.pack(fill='x', expand='True') # fill lo deja fijo a una parte de la ventana y expand permite que si se agranda la ventada con esta tambien se agrande el frame
miFrame.config(bg='blue', width='500', height='200', bd=15,relief='sunken',cursor='pirate') # relief es textura


# ----------------------------------------------------------------------------------
# esto ejecuta la apertura de una ventana NOTA: Siempre va al final
raiz.mainloop()
# NOTA: Al ejecutar el archivo inicial VentanaInicial.py abre la consola y luego la ventana, para evitar que le pase eso al usuario hay que copiar el archivo y pegarlo con la extension .pyw asi solo se ejecuta la ventana
