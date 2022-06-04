import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Menu y submenu con Tkinter y python")
ventana.geometry("600x300")



def color_amarillo():
    ventana['bg'] = 'yellow'


def color_verde():
    ventana['bg'] = 'green'


def color_azul():
    ventana['bg'] = 'blue'
    print("Hola",ventana)


def color_rojo():
    ventana['bg'] = 'red'


def color_gris():
    ventana['bg'] = 'gray'
    
def mensaje():
    answer=messagebox.askyesno("Salir","¿Desea salir?, Confirme..")
    if(answer):
        ventana.destroy()
        

def on_closing():
    if messagebox.askokcancel("Salir", "¿Desea salir?, Confirme.."):
        ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", on_closing)



mi_menu = tk.Menu(ventana)
mi_menu.add_command(label='amarillo', command=color_amarillo)
mi_menu.add_command(label='verde', command=color_verde)
mi_menu.add_command(label='azul', command=color_azul)

mi_dropdown = tk.Menu(ventana)
mi_dropdown.add_command(label='Amarillo', command=color_amarillo)
mi_dropdown.add_command(label='Verde', command=color_verde)
mi_dropdown.add_command(label='Verde', command=color_azul)
mi_dropdown = tk.Menu(mi_menu, tearoff=0)

mi_dropdown.add_command(label='Rojo', command=color_rojo)
mi_dropdown.add_command(label='Gris',command=color_gris)

mi_menu.add_cascade(label='Otros colores', menu=mi_dropdown)

mi_menu.add_command(label='salir',command=mensaje)




ventana.config(menu=mi_menu)
ventana.mainloop()
