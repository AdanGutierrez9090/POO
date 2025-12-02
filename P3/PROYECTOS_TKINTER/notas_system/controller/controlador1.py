from tkinter import messagebox
from model import usuario,nota

class Controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos} se registro correctamente con el email: {email}",title="Registro exitoso")

        else:
            messagebox.showwarning(icon="warning",message="Por favor intentelo de nuevo, no fue posible insertar el registro",title="Usuarios")

    @staticmethod
    def inicio_sesion(email,password):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f".:: {registro[1]} {registro[2]}, iniciaste sesion correctamente ::.",title="Usuarios")
        else:
            messagebox.showwarning(icon="warning",message="E-mail y/o contraseña incorrectos... vuelva a intentarlo",title="Usuarios")
        return registro [0],registro[1], registro[2]
    