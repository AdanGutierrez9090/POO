import tkinter as tk

ventana=tk.Tk()

ventana.title("Mi primera app grafica en tkinter con python")
ventana.geometry ("800x600")
ventana.resizable(False,False) #sirve para bloquear o desbloquear el modificar  el tamaño de la ventana
ventana.mainloop() #metodo que permite tener una ventana abierta e interactuar con ella