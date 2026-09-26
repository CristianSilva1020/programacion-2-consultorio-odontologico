print("========================================")
print("   CONSULTORIO ODONTOLÓGICO DR. XXX")
print("========================================")
print()

cedula = input("Ingrese la cédula del cliente: ")
nombre = input("Ingrese el nombre del cliente: ")
telefono = input("Ingrese el teléfono del cliente: ")

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

print()
print("Datos registrados:")
print("Cédula:", cedula)
print("Nombre:", nombre)
print("Teléfono:", telefono)
print("Tipo de cliente:", tipo_cliente)