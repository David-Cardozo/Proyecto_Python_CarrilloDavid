from Funciones.funcionesJson import *
from Funciones.funcionesLista import *

dataBool = True
boolGastos = True
boolCalculos = True
boolInforme = True
listaData = abrirJSONData()

while (dataBool):
    print("=========================================================================")
    print("                      Simulador de Gasto Diario                          ")
    print("=========================================================================")
    print("Seleccione una opcion:   ")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Eliminar gasto especifico")
    print("6. Actualizar gasto especifico")
    print("7. Salir")
    opcionUsu = (int(input("Escoja una opcion -Numerica- :  ")))
    print("")
    print("")

    if (opcionUsu == 1):
        print("=========================================================================")
        print("                      Registrar nuevo gasto                          ")
        print("=========================================================================")
        montoGasto = int(input("- Monto del gasto:   "))
        categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros):  ")
        descripcionGasto = input("- Descripción (opcional):   ")
        fechaGasto = input("- Fecha del gasto (DD-MM-YYYY):   ")
        print()
        confirmacion = input("Ingrese 'S' para guardar o 'C' para cancelar.   "   )
        print("=========================================================================")
        if (confirmacion.upper() == 'S'):
            diccionarioGastos={
                "id": (listaData[len(listaData)-1]["id"])+1,
                "monto": montoGasto,
                "categoria": categoriaGasto,
                "descripcion": descripcionGasto,
                "fecha": fechaGasto
            }
            listaData.append(diccionarioGastos)
            guardarJSONData(listaData)
        else:
            print("No se ha guardado el gasto")
    elif(opcionUsu == 2):
        
        while (boolGastos):

            print("")
            print("=========================================================================")
            print("                         Listar Gastos")
            print("=========================================================================")
            print("Seleccione una opcion para filtrar los gastos:   ")
            print("")
            print("1. Ver todos los gastos")
            print("2. Filtrar por categoria")
            print("3. Filtrar por rango de fechas")
            print("4. Regresar al menu principal")
            print("=========================================================================")
            opcionListarGas = (int(input("Escoja una opcion -Numerica- :  ")))
            print("")
            print("")
        
            if (opcionListarGas == 1):

                recorrerLista(listaData)

            elif(opcionListarGas == 2):

                categoria = input("Ingrese el nombre de la categoria:   ")
                recorrerCategoria(listaData, categoria)

            elif(opcionListarGas == 3):

                fechaInicio = input("Ingrese la fecha de inicio (En formato DD-MM-YYYY):  ")
                fechaFin = input("Ingrese la fecha final (En formato DD-MM-YYYY):  ")
                recorrerFecha(listaData, fechaInicio, fechaFin)

            elif(opcionListarGas == 4):

                print("")
                print("Regresando el menu principal!!!!")
                print("")
                boolGastos = False

            else:
                print("")
                print("¡Por favor escoja una de las opciones disponibles!")
                print("")

    elif(opcionUsu == 3):

        while (boolCalculos):

            print("")
            print("=========================================================================")
            print("                     Calcular Total de Gastos")
            print("=========================================================================")
            print("Seleccione el perido de calculo:   ")
            print("")
            print("1. Calcular total diario")
            print("2. Calcular total semanal")
            print("3. Calcular total mensual")
            print("4. Desglose por categoria")
            print("5. Regresar al menu principal")
            print("=========================================================================")
            opcionCalcularGas = (int(input("Escoja una opcion -Numerica- :  ")))
            print("")
            print("")

            if(opcionCalcularGas == 1):
                totalDiario = calcularGastos(listaData, "d")
                print("")
                print(f"- Total diario:   {totalDiario}")
                print("")

            elif(opcionCalcularGas == 2):
                totalSemanal = calcularGastos(listaData, "s")
                print("")
                print(f"- Total semanal:   {totalSemanal}")
                print("")

            elif(opcionCalcularGas == 3):
                totalMensual = calcularGastos(listaData, "m")
                print("")
                print(f"- Total mensual:    {totalMensual}")
                print("")
            elif(opcionCalcularGas == 4):
                print("")
                print(desgloseCategoria(listaData))
                print("")

            elif(opcionCalcularGas == 5):
                print("")
                print("Regresando el menu principal!!!!")
                print("")
                boolCalculos = False

            else:
                print("")
                print("¡Por favor escoja una de las opciones disponibles!")
                print("")
    
    elif(opcionUsu == 4):

        while (boolInforme):
            print("")
            print("")
            print("=========================================================================")
            print("                        Generar Reporte de Gastos")
            print("=========================================================================")
            print("Seleccione una opcion para filtrar los gastos:   ")
            print("")
            print("1. Reporte diario")
            print("2. Reporte semanal")
            print("3. Reporte mensual")
            print("4. Regresar al menu principal")
            print("=========================================================================")
            opcionReportes = (int(input("Escoja una opcion -Numerica- :  ")))
            print("")
            print("")

            if(opcionReportes == 1):
                reporteDiario = generarReporte(listaData, "Diario")
                print("")
                print(reporteDiario)
                print("")
            elif(opcionReportes == 2):
                reporteSemanal = generarReporte(listaData, "Semanal")
                print("")
                print(reporteSemanal)
                print("")
            elif(opcionReportes == 3):
                reporteDiario = generarReporte(listaData, "Diario")
                print("")
                print(reporteDiario)
                print("")