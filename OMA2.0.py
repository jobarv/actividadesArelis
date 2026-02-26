import time
import os
from datetime import datetime

# ==========================================
# CLASE PARA GESTIÓN DE ARCHIVOS
# ==========================================
class GestorArchivos:

    def __init__(self, fecha):
        self.fecha = fecha  # Tupla (día, mes, año)
        self.archivos_base = {
            "quejas.txt": "Registro inicial de quejas\n",
            "clientes.txt": "Base de clientes\n",
            "seguimientos.txt": "Historial de seguimientos\n",
            "reportes.txt": "Reportes generados\n"
        }
        self.crear_archivos_base()

    # Crea archivos iniciales si no existen
    def crear_archivos_base(self):
        for nombre, contenido in self.archivos_base.items():
            if not os.path.exists(nombre):
                with open(nombre, "w", encoding="utf-8") as f:
                    f.write(contenido)

    # Listar archivos disponibles
    def listar_archivos(self):
        print("\nArchivos disponibles:")
        archivos = os.listdir()
        for i, archivo in enumerate(archivos):
            if archivo.endswith(".txt"):
                print(f"{i}. {archivo}")

    # Leer archivo
    def leer_archivo(self):
        try:
            nombre = input("Ingrese el nombre del archivo a leer: ")
            with open(nombre, "r", encoding="utf-8") as f:
                print("\nContenido del archivo:\n")
                print(f.read())
        except FileNotFoundError:
            print("❌ Error: El archivo no existe.")
        except Exception as e:
            print("❌ Error inesperado:", e)

    # Escribir en archivo existente
    def escribir_archivo(self):
        try:
            nombre = input("Ingrese el archivo a modificar: ")
            texto = input("Ingrese el contenido a agregar: ")
            with open(nombre, "a", encoding="utf-8") as f:
                f.write(f"\n[{self.fecha}] {texto}")
            print("✅ Archivo actualizado correctamente.")
        except FileNotFoundError:
            print("❌ Archivo no encontrado.")
        except Exception as e:
            print("❌ Error:", e)

    # Crear nuevo archivo
    def crear_archivo(self):
        try:
            nombre = input("Ingrese nombre del nuevo archivo: ")
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(f"Archivo creado el {self.fecha}\n")
            print("✅ Archivo creado correctamente.")
        except Exception as e:
            print("❌ Error:", e)


# ==========================================
# CLASE PRINCIPAL DEL SISTEMA
# ==========================================
class SistemaOMA:

    def __init__(self):
        self.usuario = ""
        self.fecha = ()
        self.gestor = None

    # Solicita usuario y muestra bienvenida
    def login(self):
        self.usuario = input("Ingrese su nombre o nickname: ")
        mensaje = "Bienvenido al sistema OMA, " + self.usuario.upper()
        print("\n" + mensaje)

    # Simula carga del sistema
    def pantalla_carga(self):
        print("\nCargando sistema...")
        for i in range(5):
            print("Procesando" + "." * (i+1))
            time.sleep(1)

    # Solicita fecha válida y la guarda como tupla
    def solicitar_fecha(self):
        while True:
            try:
                fecha_input = input("Ingrese fecha (dd/mm/aaaa): ")
                fecha_obj = datetime.strptime(fecha_input, "%d/%m/%Y")
                self.fecha = (fecha_obj.day, fecha_obj.month, fecha_obj.year)
                break
            except ValueError:
                print("❌ Formato incorrecto. Intente nuevamente.")

    # Menú tabular con matriz
    def mostrar_menu(self):
        menu = [
            ["1", "Leer archivo"],
            ["2", "Escribir archivo"],
            ["3", "Crear archivo"],
            ["4", "Cambiar usuario"],
            ["5", "Salir"]
        ]

        print("\n===== MENÚ PRINCIPAL =====")
        print("OPCIÓN | ACCIÓN")
        for fila in menu:
            print(f"{fila[0]}      | {fila[1]}")

    # Control de tiempo de espera
    def esperar_opcion(self):
        for i in range(600):  # 10 minutos
            time.sleep(1)
            if i == 599:
                decision = input("¿Desea continuar? (si/no): ").lower()
                if decision != "si":
                    self.login()

    # Ejecuta el sistema
    def ejecutar(self):
        self.login()
        self.pantalla_carga()
        self.solicitar_fecha()
        self.gestor = GestorArchivos(self.fecha)

        while True:
            self.mostrar_menu()

            inicio = time.time()
            opcion = input("Seleccione opción: ")
            fin = time.time()

            print(f"Tiempo de selección: {round(fin - inicio, 2)} segundos")

            try:
                if opcion == "1":
                    self.gestor.listar_archivos()
                    self.gestor.leer_archivo()

                elif opcion == "2":
                    self.gestor.listar_archivos()
                    self.gestor.escribir_archivo()

                elif opcion == "3":
                    self.gestor.crear_archivo()

                elif opcion == "4":
                    self.login()

                elif opcion == "5":
                    print("Gracias por usar el sistema.")
                    break

                else:
                    print("❌ Opción inválida.")

            except Exception as e:
                print("❌ Error general:", e)


# ==========================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    sistema = SistemaOMA()
    sistema.ejecutar()