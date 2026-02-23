total_pagar = 0

print("=== Sistema de boletos del museo ===")

num_visitantes = int(input("¿Cuántos visitantes pagarán boleto? "))

for i in range(num_visitantes):
    print(f"\nVisitante #{i+1}")

    edad = int(input("Edad: "))

    # Regla: menores de 3 no pagan
    if edad < 3:
        print("Menor de 3 años → No paga boleto")
        continue  # salta al siguiente visitante

    # Determinar precio base
    if edad < 18:
        precio = 30
        es_mayor_edad = False
    else:
        precio = 45
        es_mayor_edad = True

    print("Tipo de visitante:")
    print("1 = Adulto Mayor")
    print("2 = Profesor")
    print("3 = Estudiante")
    print("4 = Ninguno")

    tipo = int(input("Seleccione opción: "))

    # Tabla de verdad (solo un descuento)
    es_adulto_mayor = tipo == 1
    es_profesor = tipo == 2
    es_estudiante = tipo == 3

    # Aplicación de descuento
    if es_adulto_mayor:
        descuento = 0.12
    elif es_profesor:
        descuento = 0.10
    elif es_estudiante:
        descuento = 0.10
    else:
        descuento = 0

    precio_final = precio * (1 - descuento)

    print(f"Precio base: ${precio}")
    print(f"Descuento aplicado: {descuento*100}%")
    print(f"Precio final: ${precio_final:.2f}")

    total_pagar += precio_final

    # Clausula break opcional
    cancelar = input("¿Desea cancelar el proceso? (s/n): ")
    if cancelar.lower() == "s":
        print("Proceso cancelado por el usuario.")
        break

print(f"\nTOTAL A PAGAR: ${total_pagar:.2f}")