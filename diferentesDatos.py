# ==========================================
# APLICACIÓN DE ESTRUCTURAS DE DATOS EN PYTHON
# ==========================================

# ----------- USO DE TUPLAS -----------
def modulo_tuplas():
    print("\n=== MÓDULO TUPLAS ===")

    # 1. Crear tupla con al menos 5 frutas
    frutas = ("manzana", "pera", "uva", "mango", "naranja")
    print("Tupla original:", frutas)

    # 2. Mostrar tercer elemento
    print("Tercer elemento:", frutas[2])

    # 3. Agregar 2 frutas por input (se crea una nueva tupla)
    f1 = input("Ingresa una fruta adicional: ")
    f2 = input("Ingresa otra fruta adicional: ")
    frutas = frutas + (f1, f2)
    print("Tupla actualizada:", frutas)

    # 4. Convertir a lista y ordenar
    lista_frutas = list(frutas)
    lista_frutas.sort()
    print("Lista ordenada:", lista_frutas)

    # 5. Función para sumar elementos de una tupla numérica
    def suma_tupla(t):
        total = 0
        for n in t:
            total += n
        return total

    # 6. Aplicar función (se crea tupla de números con longitudes de frutas)
    longitudes = tuple(len(f) for f in frutas)
    print("Longitudes de nombres:", longitudes)
    print("Suma de longitudes:", suma_tupla(longitudes))


# ----------- USO DE DICCIONARIOS -----------
def modulo_diccionarios():
    print("\n=== MÓDULO DICCIONARIOS ===")

    # 1. Crear diccionario de contactos
    contactos = {
        "Ana": "8111111111",
        "Luis": "8222222222",
        "Carlos": "8333333333"
    }
    print("Contactos iniciales:", contactos)

    # 2. Agregar contacto por input
    nombre = input("Nombre del nuevo contacto: ")
    telefono = input("Teléfono: ")
    contactos[nombre] = telefono

    print("Contactos actualizados:", contactos)

    # 3. Imprimir nombres de contactos
    print("\nLista de contactos:")
    for nombre in contactos.keys():
        print(nombre)

    # 4. Función para buscar teléfono
    def buscar_contacto(dic, nombre):
        return dic.get(nombre, "No encontrado")

    # 5. Buscar contacto
    nombre_buscar = input("\nNombre a buscar: ")
    print("Teléfono:", buscar_contacto(contactos, nombre_buscar))


# ----------- USO DE EXCEPCIONES -----------
class DivisionEntreCeroError(Exception):
    pass


def modulo_excepciones():
    print("\n=== MÓDULO EXCEPCIONES ===")

    try:
        a = int(input("Ingresa el primer número entero: "))
        b = int(input("Ingresa el segundo número entero: "))

        print("Suma:", a + b)

        if b == 0:
            raise DivisionEntreCeroError("No se puede dividir entre cero")

        print("División:", a / b)

    except ValueError:
        print("Error: Debes ingresar valores numéricos enteros.")
    except DivisionEntreCeroError as e:
        print("Error:", e)


# ----------- USO DE STRINGS -----------
def modulo_strings():
    print("\n=== MÓDULO STRINGS ===")

    # 1. Crear mensaje
    mensaje = "Python es un lenguaje poderoso y facil de aprender"
    print("Mensaje:", mensaje)

    # 2. Longitud
    print("Longitud:", len(mensaje))

    # 3. Mayúsculas
    print("Mayúsculas:", mensaje.upper())

    # 4. Reemplazo
    nuevo = mensaje.replace("Python", "Este lenguaje")
    print("Mensaje modificado:", nuevo)

    # 5. Función contar palabras
    def contar_palabras(texto):
        return len(texto.split())

    # 6. Aplicar función
    print("Cantidad de palabras:", contar_palabras(mensaje))


# ----------- MENÚ PRINCIPAL -----------
def menu():
    while True:
        print("\n==========================")
        print("   MENÚ PRINCIPAL")
        print("==========================")
        print("1. Trabajar con Tuplas")
        print("2. Trabajar con Diccionarios")
        print("3. Manejo de Excepciones")
        print("4. Manejo de Strings")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            modulo_tuplas()
        elif opcion == "2":
            modulo_diccionarios()
        elif opcion == "3":
            modulo_excepciones()
        elif opcion == "4":
            modulo_strings()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


# Ejecutar programa
menu()