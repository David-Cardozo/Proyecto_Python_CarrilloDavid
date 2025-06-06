from Funciones.funcionesJson import *
from Funciones.funcionesLista import *

dataBool = True
boolGastos = True
boolCalculos = True
boolInforme = True
listaData = abrirJSONData()
informes = abrirJSONInfo()

while (dataBool):
    print("=========================================================================")
    print("                      Simulador de Gasto Diario                          ")
    print("=========================================================================")
    print("Seleccione una opcion:   ")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Eliminar gasto especifico (Segun ID)")
    print("6. Actualizar gasto especifico (Segun ID)")
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
                print("Desea mostrar el informe en pantalla o guardarlo en JSON:")
                print("1. Mostrar en pantalla")
                print("2. Guardar en JSON")
                opcionGuardado = (int(input("Escoja una opcion -Numerica- :  ")))
                print("")

                if(opcionGuardado == 1):
                    print(reporteDiario)
                    print("")
                elif(opcionGuardado == 2):
                    dicData = {'informe' : reporteDiario}
                    informes.append(dicData)
                    guardarJSONInfo(informes)
                    print("El informe ha sido guardado en informes.json")
                    print("")
                else:
                    print("Ingrese una opcion valida!")

            elif(opcionReportes == 2):
                reporteSemanal = generarReporte(listaData, "Semanal")

                print("")
                print("Desea mostrar el informe en pantalla o guardarlo en JSON:")
                print("1. Mostrar en pantalla")
                print("2. Guardar en JSON")
                opcionGuardado = (int(input("Escoja una opcion -Numerica- :  ")))
                print("")

                if (opcionGuardado == 1):
                    print(reporteSemanal)
                    print("")
                elif(opcionGuardado == 2):
                    dicData = {'informe' : reporteSemanal}
                    informes.append(dicData)
                    guardarJSONInfo(informes)
                    print("El informe ha sido guardado en informes.json")
                    print("")
                else:
                    print("Ingrese una opcion valida!")

            elif(opcionReportes == 3):
                reporteMensual = generarReporte(listaData, "Mensual")

                print("")
                print("Desea mostrar el informe en pantalla o guardarlo en JSON:")
                print("1. Mostrar en pantalla")
                print("2. Guardar en JSON")
                opcionGuardado = (int(input("Escoja una opcion -Numerica- :  ")))
                print("")

                if (opcionGuardado == 1):
                    print(reporteMensual)
                    print("")
                elif(opcionGuardado == 2):
                    dicData = {'informe' : reporteMensual}
                    informes.append(dicData)
                    guardarJSONInfo(informes)
                    print("El informe ha sido guardado en informes.json")
                    print("")
                else:
                    print("Ingrese una opcion valida!")
            elif (opcionReportes == 4):
                print("")
                print("Regresando el menu principal!!!!")
                print("")
                boolInforme = False
    
    elif (opcionUsu == 5):
        print("")
        print("")
        print("=========================================================================")
        print("                        Eliminar gasto individual")
        print("=========================================================================")
        print("")
        print("")
        recorrerLista(listaData)
        print("")
        print("")
        opcionEliminar = int(input("Por favor ingresar el ID del gasto a eliminar:"))
        mostrarGasto(listaData, opcionEliminar)
        opcionComprobar = int(input("¿Estás seguro de eliminar a esta persona? (1.Si --- 2.No):"))

        if (opcionComprobar == 1):
            temp = listaData.pop(opcionEliminar-1)
            guardarJSONLogs(temp)
            guardarJSONData(listaData)
            print("")
            print("")
            print("Usuario eliminado!")
            print("")
            print("")
        else:
            print("")
            print("")
            print("Gracias por hacer la confirmacion")
            print("")
            print("")
    
    elif (opcionUsu == 6):
        print("")
        print("")
        print("=========================================================================")
        print("                        Actualizar gasto")
        print("=========================================================================")
        print("")
        print("")
        opcionActualizar = int(input("Por favor ingresar el id del gasto deseado:"))
        mostrarGasto(listaData, opcionActualizar-1)
        userTemp = listaData[opcionActualizar-1]["id"]
        montoTemp = int(input("Ingrese el monto actualizado:   "))
        categoriaTemp = input("Ingrese la categoria actualizada:   ")
        descripcionTemp = input("Ingrese la descripcion actualizada:   ")
        fechaTemp = input("Ingrese la fecha actualizada (DD-MM-YYYY):   ")
        dicAgregar = {"id" : userTemp, "monto" : montoTemp, "categoria" : categoriaTemp, "descripcion" : descripcionTemp, "fecha" : fechaTemp}
        listaData[opcionActualizar-1] = dicAgregar
        guardarJSONData(listaData)
        print("")
        print("")
        print("El usuario ha sido actualizado!!!")
        print("")
        print("")

    elif (opcionUsu == 7):
        print("Hasta pronto!")
        dataBool = False
    
    else: 
        print("Ingrese una opcion valida!")