from tkinter import *

ventana=Tk()

ventana.title("Mainloop")
ventana.geometry("800x600")

marco=Frame(ventana)
marco.config(
    bg="#07CEF1",
    bd=10,
    height=400,
    width=600,
    relief=RAISED
)

marco.pack(
    padx=50,
    pady=50
)

ventana.mainloop()