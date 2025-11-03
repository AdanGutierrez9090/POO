from estudiante.estudiantes import Estudiante
import os

class App:
    def __init__(self):
        self.opcion = None

    def borrarPantalla(self):
        os.system("cls" if os.name == "nt" else "clear")

    def esperarTecla(self):
        input("\nPresiona ENTER para continuar...")

    def datos_estudiante(self, tipo):
        if tipo in ["crear", "actualizar"]:
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota: "))
            return nombre, nota
        elif tipo == "actualizar_id":
            id_est = int(input("Ingrese el ID del estudiante a actualizar: "))
            return id_est
        elif tipo == "eliminar":
            id_est = int(input("Ingrese el ID del estudiante a eliminar: "))
            return id_est
        return None

    def respuesta_sql(self, respuesta):
        if respuesta:
            print("✅ Operación realizada con éxito.")
        else:
            print("❌ Ocurrió un error en la operación.")
        self.esperarTecla()

    def menu_acciones(self, tipo):
        if tipo == "crear":
            nombre, nota = self.datos_estudiante("crear")
            estudiante = Estudiante(nombre, nota)
            self.respuesta_sql(estudiante.crear())

        elif tipo == "mostrar":
            estudiante.mostrar()
            self.esperarTecla()

        elif tipo == "actualizar":
            id_est = self.datos_estudiante("actualizar_id")
            nombre, nota = self.datos_estudiante("actualizar")
            estudiante = Estudiante(nombre, nota, id_est)
            self.respuesta_sql(estudiante.actualizar())

        elif tipo == "eliminar":
            id_est = self.datos_estudiante("eliminar")
            self.respuesta_sql(Estudiante.eliminar(id_est))

        elif tipo == "nota":
            nombre, nota = self.datos_estudiante("crear")
            estudiante = Estudiante(nombre, nota)
            estudiante.mostrar_nota()
            self.esperarTecla()

        else:
            print("❌ Tipo de acción no reconocido.")
            self.esperarTecla()

    def menu_estudiante(self):
        while True:
            self.borrarPantalla()
            print("===== 📚 MENÚ DE ESTUDIANTES =====")
            print("1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Actualizar estudiante")
            print("4. Eliminar estudiante")
            print("5. Verificar aprobación")
            print("6. Volver al menú principal")

            opcion = input("\nSelecciona una opción (1-6): ")

            if opcion == "1":
                self.menu_acciones("crear")
            elif opcion == "2":
                self.menu_acciones("mostrar")
            elif opcion == "3":
                self.menu_acciones("actualizar")
            elif opcion == "4":
                self.menu_acciones("eliminar")
            elif opcion == "5":
                self.menu_acciones("nota")
            elif opcion == "6":
                print("🔙 Volviendo al menú principal...")
                self.esperarTecla()
                break
            else:
                print("❌ Opción inválida.")
                self.esperarTecla()

    def main(self):
        while True:
            self.borrarPantalla()
            print("===== 🎓 MENÚ PRINCIPAL =====")
            print("1. Estudiante")
            print("2. Salir")

            opcion = input("\nSelecciona una opción (1-2): ")

            if opcion == "1":
                self.menu_estudiante()
            elif opcion == "2":
                print("👋 Saliendo del programa...")
                break
            else:
                print("❌ Opción inválida.")
                self.esperarTecla()

if __name__ == "__main__":
    app = App()
    app.main()

