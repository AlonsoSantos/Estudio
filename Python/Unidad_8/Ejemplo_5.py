# MENU
from tkinter import *


# VENTANAS EMERGENTES----------------------------------------------------------------------
from tkinter import messagebox
from tkinter import filedialog

# el primer parametro es el titulo de la ventana emergente y el segundo la informacion dentro de esta
def infoAdicional():
    messagebox.showinfo('Programa de Alonso', 'Programa 2020')

def infoLicencia():
    messagebox.showwarning('Licencia','Licencia activada hasta el 2020')

def salirApp():
    # valor = messagebox.askquestion('Salir','¿Estás seguro que deseas salir?')
    # if valor == 'yes':
    #     raiz.destroy()
    valor = messagebox.askokcancel('Salir','¿Estás seguro que deseas salir?')
    if valor == True:
        raiz.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel('Reintentar','No es posible cerrar el documento')
    if valor == False:
        raiz.destroy()

def abreArchivo():
    archivo = filedialog.askopenfilename(title='Abrir', initialdir='/', filetypes=(('Fichero de Excel','*.xlsx'),('Fichero de texto','*.txt'),('Todos los ficheros','*')))
    print(archivo)
# -----------------------------------------------------------------------------------------

raiz = Tk()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Abrir', command=abreArchivo)
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar como...')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=cerrarDocumento)
archivoMenu.add_command(label='Salir', command=salirApp)

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label='Copiar')
edicionMenu.add_command(label='Cortar')
edicionMenu.add_command(label='Pegar')

herramientaMenu=Menu(barraMenu, tearoff=0)
herramientaMenu.add_command(label='Reemplazar')

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label='Licencia', command=infoLicencia)
ayudaMenu.add_command(label='Acerca de...', command=infoAdicional)

barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=edicionMenu)
barraMenu.add_cascade(label='Herramientas', menu=herramientaMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

raiz.mainloop()