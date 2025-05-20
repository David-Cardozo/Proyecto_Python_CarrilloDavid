from Funciones.funcionesJson import *
from Funciones.funcionesLista import *

dataBool = True
listaData = abrirJSON()

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

    if (opcionUsu == 1):
        print("=========================================================================")
        print("                      Registrar nuevo gasto                          ")
        print("=========================================================================")
        montoGasto = int(input("- Monto del gasto:   "))
        categoriaGasto = input(" - Categoría (ej. comida, transporte, entretenimiento, otros):  ")
        descripcionGasto = input("- Descripción (opcional):   ")
        fechaGasto = input("- Fecha del gasto (DD-MM-YYYY):   ")
        print()
        confirmacion = input("Ingrese 'S' para guardar o 'C' para cancelar."   )
        print("=========================================================================")
        if (confirmacion.upper() == 'S'):
            diccionarioGastos={
                "id": (listaData[len(listaData)-1]["id"])+1,
                "monto": montoGasto,
                "Categoria": categoriaGasto,
                "Descripcion": descripcionGasto,
                "Fecha": fechaGasto
            }
            listaData.append(diccionarioGastos)
            guardarJSON(listaData)
        else:
            print("No se ha guardado el gasto")
    elif(opcionUsu == 2):
        recorrerLista(listaData)