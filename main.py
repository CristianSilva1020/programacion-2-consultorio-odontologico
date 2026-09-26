print("========================================")
print("   CONSULTORIO ODONTOLÓGICO DR. XXX")
print("========================================")
print()

#Datos básicos del cliente
cedula = input("Ingrese la cédula del cliente: ")
nombre = input("Ingrese el nombre del cliente: ")
telefono = input("Ingrese el teléfono del cliente: ")

#Tipo de cliente
print()
print("Tipo de cliente:")
print("1. Particular")
print("2. EPS")
print("3. Prepagada")

while True:
    opcion_cliente = input("Seleccione una opción: ")

    if opcion_cliente == "1":
        tipo_cliente = "Particular"
        break
    elif opcion_cliente == "2":
        tipo_cliente = "EPS"
        break
    elif opcion_cliente == "3":
        tipo_cliente = "Prepagada"
        break
    else:
        print("Opción inválida. Intente nuevamente.")

#Tipo de atención
print()
print("Tipo de atención:")
print("1. Limpieza")
print("2. Calzas")
print("3. Extracción")
print("4. Diagnóstico")

while True:
    opcion_atencion = input("Seleccione una opción: ")

    if opcion_atencion == "1":
        tipo_atencion = "Limpieza"
        break
    elif opcion_atencion == "2":
        tipo_atencion = "Calzas"
        break
    elif opcion_atencion == "3":
        tipo_atencion = "Extracción"
        break
    elif opcion_atencion == "4":
        tipo_atencion = "Diagnóstico"
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Cantidad
if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnóstico":
    cantidad = 1
    print()
    print("La cantidad para", tipo_atencion, "es automáticamente 1.")
else:
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor que cero.")

        except ValueError:
            print("Debe ingresar un número entero válido.")

# Prioridad de atención
print()
print("Prioridad de atención:")
print("1. Normal")
print("2. Urgente")

while True:
    opcion_prioridad = input("Seleccione una opción: ")

    if opcion_prioridad == "1":
        prioridad = "Normal"
        break
    elif opcion_prioridad == "2":
        prioridad = "Urgente"
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Fecha de la cita
print()
fecha_cita = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")


# Datos registrados
print()
print("Datos registrados:")
print("Cédula:", cedula)
print("Nombre:", nombre)
print("Teléfono:", telefono)
print("Tipo de cliente:", tipo_cliente)
print("Tipo de atención:", tipo_atencion)
print("Cantidad:", cantidad)
print("Prioridad:", prioridad)
print("Fecha de la cita:", fecha_cita)
