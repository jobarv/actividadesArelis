print("=== Tabla de Pitágoras ===")

# Solicitar factores
filas = int(input("Ingresa el primer factor (filas): "))
columnas = int(input("Ingresa el segundo factor (columnas): "))

print("\nTabla de multiplicar:\n")

# Mostrar encabezado superior
print("    ", end="")
for j in range(1, columnas + 1):
    print(f"{j:4}", end="")
print()

# Línea separadora
print("    " + "----" * columnas)

# Generar tabla
for i in range(1, filas + 1):
    print(f"{i:3}|", end="")
    for j in range(1, columnas + 1):
        print(f"{i * j:4}", end="")
    print()