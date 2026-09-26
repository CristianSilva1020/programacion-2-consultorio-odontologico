print("========================================")
print("   CONSULTORIO ODONTOLÓGICO DR. XXX")
print("========================================")
print()

# Lista donde se almacenarán todos los clientes
clientes = []

while True:

    # Datos básicos del cliente
    cedula = input("Ingrese la cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    # Tipo cliente
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

    # Tipo de atención
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

    # Calcular valor de la cita y valor unitario de la atención
    if tipo_cliente == "Particular":
        valor_cita = 80000

        if tipo_atencion == "Limpieza":
            valor_atencion_unitario = 60000
        elif tipo_atencion == "Calzas":
            valor_atencion_unitario = 80000
        elif tipo_atencion == "Extracción":
            valor_atencion_unitario = 100000
        elif tipo_atencion == "Diagnóstico":
            valor_atencion_unitario = 50000

    elif tipo_cliente == "EPS":
        valor_cita = 5000

        if tipo_atencion == "Limpieza":
            valor_atencion_unitario = 0
        elif tipo_atencion == "Calzas":
            valor_atencion_unitario = 40000
        elif tipo_atencion == "Extracción":
            valor_atencion_unitario = 40000
        elif tipo_atencion == "Diagnóstico":
            valor_atencion_unitario = 0

    elif tipo_cliente == "Prepagada":
        valor_cita = 30000

        if tipo_atencion == "Limpieza":
            valor_atencion_unitario = 0
        elif tipo_atencion == "Calzas":
            valor_atencion_unitario = 10000
        elif tipo_atencion == "Extracción":
            valor_atencion_unitario = 10000
        elif tipo_atencion == "Diagnóstico":
            valor_atencion_unitario = 0

    # Calcular valores finales
    valor_atencion = valor_atencion_unitario * cantidad
    valor_total = valor_cita + valor_atencion

    # Crear registro del cliente
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha_cita": fecha_cita,
        "valor_cita": valor_cita,
        "valor_atencion_unitario": valor_atencion_unitario,
        "valor_atencion": valor_atencion,
        "valor_total": valor_total
    }

    # Guardar cliente en la lista
    clientes.append(cliente)

    # Mostrar resumen de la cita
    print()
    print("========================================")
    print("RESUMEN DE LA CITA")
    print("========================================")
    print("Cédula:", cedula)
    print("Nombre:", nombre)
    print("Teléfono:", telefono)
    print("Tipo de cliente:", tipo_cliente)
    print("Tipo de atención:", tipo_atencion)
    print("Cantidad:", cantidad)
    print("Prioridad:", prioridad)
    print("Fecha de la cita:", fecha_cita)
    print("Valor de la cita: $", valor_cita)
    print("Valor unitario de la atención: $", valor_atencion_unitario)
    print("Valor total de la atención: $", valor_atencion)
    print("Valor total a pagar: $", valor_total)

    # Preguntar si desea registrar otro cliente
    print()
    while True:
        continuar = input("¿Desea registrar otro cliente? (s/n): ").lower()

        if continuar == "s" or continuar == "n":
            break
        else:
            print("Opción inválida. Escriba s para sí o n para no.")

    if continuar == "n":
        break

    print()

# Calculo resultados generales
ingresos_totales = 0
clientes_extraccion = 0

for cliente in clientes:
    ingresos_totales = ingresos_totales + cliente["valor_total"]

    if cliente["tipo_atencion"] == "Extracción":
        clientes_extraccion = clientes_extraccion + 1

# Mostrar resultados generales
print()
print("========================================")
print("RESUMEN GENERAL")
print("========================================")
print("Total de clientes:", len(clientes))
print("Ingresos totales recibidos: $", ingresos_totales)
print("Número de clientes para extracción:", clientes_extraccion)

# Ordenamos clientes de mayor a menor por valor de la atención
for i in range(len(clientes) - 1):
    for j in range(len(clientes) - 1 - i):

        if clientes[j]["valor_atencion"] < clientes[j + 1]["valor_atencion"]:
            auxiliar = clientes[j]
            clientes[j] = clientes[j + 1]
            clientes[j + 1] = auxiliar

# Clientes ordenados

print()
print("========================================")
print("CLIENTES ORDENADOS POR VALOR DE ATENCIÓN")
print("========================================")

for cliente in clientes:
    print(
        "Cédula:", cliente["cedula"],
        "- Nombre:", cliente["nombre"],
        "- Atención:", cliente["tipo_atencion"],
        "- Valor atención: $", cliente["valor_atencion"]
    )

    # Buscar cliente por cédula
print()
print("========================================")
print("BÚSQUEDA DE CLIENTE")
print("========================================")

cedula_buscar = input("Ingrese la cédula del cliente que desea buscar: ")

cliente_encontrado = None

for cliente in clientes:
    if cliente["cedula"] == cedula_buscar:
        cliente_encontrado = cliente
        break

if cliente_encontrado is not None:
    print()
    print("Cliente encontrado:")
    print("Cédula:", cliente_encontrado["cedula"])
    print("Nombre:", cliente_encontrado["nombre"])
    print("Teléfono:", cliente_encontrado["telefono"])
    print("Tipo de cliente:", cliente_encontrado["tipo_cliente"])
    print("Tipo de atención:", cliente_encontrado["tipo_atencion"])
    print("Cantidad:", cliente_encontrado["cantidad"])
    print("Prioridad:", cliente_encontrado["prioridad"])
    print("Fecha de la cita:", cliente_encontrado["fecha_cita"])
    print("Valor de la cita: $", cliente_encontrado["valor_cita"])
    print("Valor unitario de la atención: $", cliente_encontrado["valor_atencion_unitario"])
    print("Valor total de la atención: $", cliente_encontrado["valor_atencion"])
    print("Valor total a pagar: $", cliente_encontrado["valor_total"])
else:
    print()
    print("No se encontró un cliente con la cédula ingresada.")