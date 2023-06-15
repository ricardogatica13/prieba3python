#lista para almacenar los datos de los afiliados
afiliados = []

# Función para validar el Rut
def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) < 2:
        return False
    cuerpo = rut[:-1]
    dv = rut[-1].upper()
    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2
    resultado = 11 - (suma % 11)
    if resultado == 11:
        resultado = "0"
    elif resultado == 10:
        resultado = "K"
    else:
        resultado = str(resultado)
    return resultado == dv



# Función para grabar los datos de una persona
def agregarAfiliado():
    rut = input("Ingrese el Rut de la persona: ")
    while not validar_rut(rut):
        print("Rut inválido. Intente nuevamente.")
        rut = input("Ingrese el Rut de la persona: ")

    nombre = input("Ingrese el Nombre de la persona: ")
    edad = int(input("Ingrese la Edad de la persona: "))
    while edad <= 18:
        print("La edad debe ser mayor a 18 años. Intente nuevamente.")
        edad = int(input("Ingrese la Edad de la persona: "))

    estado_civil = input("Ingrese el Estado Civil de la persona (C = Casado, S = Soltero, V = Viudo): ")
    while estado_civil not in ['C', 'S', 'V']:
        print("Estado civil inválido. Intente nuevamente.")
        estado_civil = input("Ingrese el Estado Civil de la persona (C = Casado, S = Soltero, V = Viudo): ")

    fecha_afiliacion = input("Ingrese la Fecha de Afiliación de la persona: ")

    afiliado = {
        'Rut': rut,
        'Nombre': nombre,
        'Edad': edad,
        'Estado Civil': estado_civil,
        'Fecha de Afiliación': fecha_afiliacion
    }
    afiliados.append(afiliado)
    print("Registro almacenado exitosamente.")

# Función para buscar una persona por su Rut
def buscarAfiliado():
    rut = input("Ingrese el Rut de la persona a buscar: ")
    encontrado = False
    for afiliado in afiliados:
        if afiliado['Rut'] == rut:
            print("---- Información de la Persona ----")
            print("Rut:", afiliado['Rut'])
            print("Nombre:", afiliado['Nombre'])
            print("Edad:", afiliado['Edad'])
            print("Estado Civil:", afiliado['Estado Civil'])
            print("Fecha de Afiliación:", afiliado['Fecha de Afiliación'])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ninguna persona con ese Rut.")

# Función para listar únicamente solteros
def listarSolteros():
    print('incompleta')