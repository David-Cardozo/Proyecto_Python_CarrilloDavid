from dataProyect.datos import *

from dataProyect.logs import *

dataBool = True

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