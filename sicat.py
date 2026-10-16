# SICAT - Sistema Integral de Control de Asistencia y Tardanzas
# Proyecto academico: Fundamentos de Programacion 1
# Los datos se mantienen en memoria mientras el programa esta abierto.

codigos = []
nombres = []
reg_codigos = []
reg_fechas = []
reg_entradas = []
reg_salidas = []
reg_trabajados = []
reg_tardanzas = []
reg_adicionales = []


def convertir_minutos(hora):
    # Formato esperado: HH:MM
    if len(hora) != 5 or hora[2:3] != ":":
        return -1
    hh = hora[0:2]
    mm = hora[3:5]
    if not hh.isdigit() or not mm.isdigit():
        return -1
    horas = int(hh)
    minutos = int(mm)
    if horas > 23 or minutos > 59:
        return -1
    return horas * 60 + minutos


def mostrar_tiempo(minutos):
    return str(minutos // 60) + " h " + str(minutos % 60) + " min"


def buscar_trabajador(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1


def registrar_trabajador():
    print("\n--- REGISTRAR TRABAJADOR ---")
    codigo = input("Codigo del trabajador: ").strip()
    nombre = input("Nombre del trabajador: ").strip()
    if codigo == "" or nombre == "":
        print("Error: el codigo y el nombre son obligatorios.")
    elif buscar_trabajador(codigo) != -1:
        print("Error: ese codigo ya esta registrado.")
    else:
        codigos.append(codigo)
        nombres.append(nombre)
        print("Trabajador registrado correctamente.")


def registrar_asistencia():
    print("\n--- REGISTRAR ASISTENCIA ---")
    codigo = input("Codigo del trabajador: ").strip()
    posicion = buscar_trabajador(codigo)
    if posicion == -1:
        print("Error: el trabajador no existe.")
        return

    fecha = input("Fecha de asistencia (DD/MM/AAAA): ").strip()
    if len(fecha) != 10 or fecha[2:3] != "/" or fecha[5:6] != "/" or not (fecha[0:2] + fecha[3:5] + fecha[6:10]).isdigit():
        print("Error: ingrese la fecha con el formato DD/MM/AAAA.")
        return
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
        print("Error: fecha fuera de rango.")
        return

    for i in range(len(reg_codigos)):
        if reg_codigos[i] == codigo and reg_fechas[i] == fecha:
            print("Error: ya existe una asistencia para este trabajador y fecha.")
            return

    entrada_programada = convertir_minutos(input("Ingreso programado (HH:MM): ").strip())
    salida_programada = convertir_minutos(input("Salida programada (HH:MM): ").strip())
    entrada_real = convertir_minutos(input("Ingreso real (HH:MM): ").strip())
    salida_real = convertir_minutos(input("Salida real (HH:MM): ").strip())
    if entrada_programada == -1 or salida_programada == -1 or entrada_real == -1 or salida_real == -1:
        print("Error: horario invalido. Use HH:MM en formato de 24 horas.")
        return

    descanso_texto = input("Minutos de descanso: ").strip()
    if not descanso_texto.isdigit():
        print("Error: el descanso debe ser un numero entero no negativo.")
        return
    descanso = int(descanso_texto)

    # Alcance de esta version: jornadas que empiezan y terminan el mismo dia.
    if salida_programada <= entrada_programada or salida_real <= entrada_real:
        print("Error: la salida debe ser posterior al ingreso (mismo dia).")
        return
    if descanso >= salida_real - entrada_real or descanso >= salida_programada - entrada_programada:
        print("Error: el descanso debe ser menor que ambas jornadas.")
        return

    tiempo_trabajado = salida_real - entrada_real - descanso
    tiempo_programado = salida_programada - entrada_programada - descanso
    tardanza = 0
    if entrada_real > entrada_programada:
        tardanza = entrada_real - entrada_programada
    adicional = 0
    if tiempo_trabajado > tiempo_programado:
        adicional = tiempo_trabajado - tiempo_programado

    reg_codigos.append(codigo)
    reg_fechas.append(fecha)
    reg_entradas.append(entrada_real)
    reg_salidas.append(salida_real)
    reg_trabajados.append(tiempo_trabajado)
    reg_tardanzas.append(tardanza)
    reg_adicionales.append(adicional)

    print("\nAsistencia registrada para:", nombres[posicion])
    print("Fecha:", fecha)
    print("Tiempo trabajado:", mostrar_tiempo(tiempo_trabajado))
    print("Tardanza:", tardanza, "minutos")
    if tardanza > 0:
        print("Estado: Tardanza")
    else:
        print("Estado: Puntual")
    print("Tiempo adicional:", mostrar_tiempo(adicional))
    print("Nota: tiempo adicional no equivale automaticamente a horas extras pagables.")


def consultar_asistencias():
    print("\n--- CONSULTAR ASISTENCIAS ---")
    if len(reg_codigos) == 0:
        print("Todavia no hay asistencias registradas.")
        return
    codigo = input("Codigo del trabajador (Enter para todos): ").strip()
    if codigo != "" and buscar_trabajador(codigo) == -1:
        print("El trabajador no existe.")
        return
    encontrados = 0
    for i in range(len(reg_codigos)):
        if codigo == "" or reg_codigos[i] == codigo:
            posicion = buscar_trabajador(reg_codigos[i])
            print("\nTrabajador:", nombres[posicion], "| Codigo:", reg_codigos[i])
            print("Fecha:", reg_fechas[i])
            print("Ingreso real:", mostrar_tiempo(reg_entradas[i]))
            print("Salida real:", mostrar_tiempo(reg_salidas[i]))
            print("Trabajado:", mostrar_tiempo(reg_trabajados[i]))
            print("Tardanza:", reg_tardanzas[i], "min | Adicional:", mostrar_tiempo(reg_adicionales[i]))
            encontrados += 1
    if encontrados == 0:
        print("No hay asistencias para ese trabajador.")


def resumen_general():
    print("\n--- RESUMEN GENERAL ---")
    if len(reg_codigos) == 0:
        print("No hay registros para analizar.")
        return
    total_trabajado = 0
    total_tardanza = 0
    total_adicional = 0
    jornadas_tarde = 0
    for i in range(len(reg_codigos)):
        total_trabajado += reg_trabajados[i]
        total_tardanza += reg_tardanzas[i]
        total_adicional += reg_adicionales[i]
        if reg_tardanzas[i] > 0:
            jornadas_tarde += 1
    print("Trabajadores registrados:", len(codigos))
    print("Jornadas registradas:", len(reg_codigos))
    print("Tiempo total trabajado:", mostrar_tiempo(total_trabajado))
    print("Tardanza acumulada:", total_tardanza, "minutos")
    print("Jornadas con tardanza:", jornadas_tarde)
    print("Tiempo adicional acumulado:", mostrar_tiempo(total_adicional))


def menu():
    opcion = ""
    while opcion != "5":
        print("\n====== SICAT ======")
        print("1. Registrar trabajador")
        print("2. Registrar asistencia")
        print("3. Consultar asistencias")
        print("4. Resumen general")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            registrar_asistencia()
        elif opcion == "3":
            consultar_asistencias()
        elif opcion == "4":
            resumen_general()
        elif opcion == "5":
            print("Gracias por utilizar SICAT.")
        else:
            print("Opcion invalida. Intente nuevamente.")


menu()
