from cProfile import label
from tkinter import *

ventana=Tk()

ventana.title("Etiquetas")
ventana.geometry("800x600")

#etiquetas o label

etiqueta1=Label(ventana,text="Nombre de la persona").pack()

marco1=Frame(ventana,bg="#515122", width=200, height=100)
marco1.pack_propagate(False)
marco1.pack()
etiqueta2=Label(marco1,text="soy una etiqueta dentro de un marco",bg="#412444").pack()





ventana.mainloop()