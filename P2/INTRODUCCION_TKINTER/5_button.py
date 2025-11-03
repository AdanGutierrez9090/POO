from cProfile import label
from tkinter import *

def cambiarTexto():
    mensajeCambiante.config(text="Soy el texto cambiado")

ventana=Tk()
ventana.title("uso de botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulo=Label(frame_principal,text="uso de botones")
label_titulo.config(
    bg="silver",
    width=20,
)

label_titulo.pack(pady=10)

mensajeCambiante=Label(ventana,text="texto original")
mensajeCambiante.pack()

boton_cambiar=Button(ventana,text="cambiar texto",command=cambiarTexto)
boton_cambiar



ventana.mainloop()