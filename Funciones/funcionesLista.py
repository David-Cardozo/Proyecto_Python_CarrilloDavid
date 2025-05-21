from datetime import datetime

# Esta funcion recorrera toda la lista en la cual se almacena nuestro diccionario
# e imprimira todos los datos
def recorrerLista (listaRecorrer):

    print("=========================================================================")
    print("                      Listado de todos los gastos")
    print("=========================================================================")
    print("")

    for i in range(len(listaRecorrer)):

        print("=========================================================================")
        print("- Gasto N°", listaRecorrer[i]["id"])
        print("- Monto de gasto:   ", listaRecorrer[i]["monto"])
        print("- Categoria de gasto:   ", listaRecorrer[i]["categoria"])
        print("- Descripcion de gasto:   ", listaRecorrer[i]["descripcion"])
        print("- Fecha de gasto:   ", listaRecorrer[i]["fecha"])
        print("=========================================================================")

# Esta funcion recorrera toda la lista en la cual se almacena nuestro diccionario
# e imprimira todos los datos segun el parametro categoria
def recorrerCategoria(listaRecorrer, categoria):

    print("=========================================================================")
    print(f"                    Filtro por categoria: {categoria}")
    print("=========================================================================")
    print("")

    for i in range(len(listaRecorrer)):
        if ((listaRecorrer[i]["categoria"]) == categoria):

            print("=========================================================================")
            print("- Gasto N°", listaRecorrer[i]["id"])
            print("- Monto de gasto:   ", listaRecorrer[i]["monto"])
            print("- Categoria de gasto:   ", listaRecorrer[i]["categoria"])
            print("- Descripcion de gasto:   ", listaRecorrer[i]["descripcion"])
            print("- Fecha de gasto:   ", listaRecorrer[i]["fecha"])
            print("=========================================================================")

# Esta funcion recorrera toda la lista en la cual se almacena nuestro diccionario
# e imprimira todos los datos segun los 2 parametros de fechas
def recorrerFecha(listaRecorrer, fechaInicio, fechaFin):
    fechaInicio = datetime.strptime(fechaInicio, "%d-%m-%Y")
    fechaFin = datetime.strptime(fechaFin, "%d-%m-%Y")

    print("=========================================================================")
    print(f"         Filtro por fechas de: {fechaInicio} a {fechaFin}")
    print("=========================================================================")
    print("")

    for i in range(len(listaRecorrer)):
        fechaGuia = datetime.strptime(listaRecorrer[i]["fecha"], "%d-%m-%Y")

        if(fechaInicio <= fechaGuia <= fechaFin):

            print("=========================================================================")
            print("- Gasto N°", listaRecorrer[i]["id"])
            print("- Monto de gasto:   ", listaRecorrer[i]["monto"])
            print("- Categoria de gasto:   ", listaRecorrer[i]["categoria"])
            print("- Descripcion de gasto:   ", listaRecorrer[i]["descripcion"])
            print("- Fecha de gasto:   ", listaRecorrer[i]["fecha"])
            print("=========================================================================")

# Esta funcion recorrera toda la lista en la cual se almacena nuestro diccionario
# y calculara el total de gastos segun el x tiempo requerido
def calcularGastos (listaRecorrer, tiempoX):
    today = datetime.now()
    total = 0

    for i in range(len(listaRecorrer)):
        
        categoria = listaRecorrer[i]["categoria"]
        montoCategoria = listaRecorrer[i]["monto"]
        fechaGuia = datetime.strptime(listaRecorrer[i]["fecha"], "%d-%m-%Y")

        # d = Diario
        if(tiempoX == "d"):
            if(fechaGuia.date() == today.date()):
                total += listaRecorrer[i]["monto"]
                print(f"La categoria {categoria} tiene un monto de: {montoCategoria}")
                
        # s = Semanal   
        elif(tiempoX == "s"):    
            if((today - fechaGuia).days <= 7):
                total += listaRecorrer[i]["monto"]
                print(f"La categoria {categoria} tiene un monto de: {montoCategoria}")
        #m = mensual
        elif(tiempoX == "m"):
            if(fechaGuia.year == today.year and fechaGuia.month == today.month):
                total += listaRecorrer[i]["monto"]
                print(f"La categoria {categoria} tiene un monto de: {montoCategoria}")
    return total

def desgloseCategoria (listaRecorrer):
    for i in range(len(listaRecorrer)):
        
        print("=========================================================================")
        print("- Categoria:   ", listaRecorrer[i]["categoria"])
        print("- Monto:   ", listaRecorrer[i]["monto"])
        print("=========================================================================")

def generarReporte(listaRecorrer, tipoInforme):
    text = f"====== Informe {tipoInforme} ======"
    print(text)

    today = datetime.now()
    total = 0

    for i in range(len(listaRecorrer)):
        
        fechaGuia = datetime.strptime(listaRecorrer[i]["fecha"], "%d-%m-%Y")

        # d = Diario
        if(tipoInforme == "Diario"):
            if(fechaGuia.date() == today.date()):
                total += listaRecorrer[i]["monto"]

                text += f"Gasto N° {listaRecorrer[i]["id"]}"
                
                
        # s = Semanal   
        elif(tipoInforme == "Semanal"):    
            if((today - fechaGuia).days <= 7):
                total += listaRecorrer[i]["monto"]
               
        #m = mensual
        elif(tipoInforme == "Mensual"):
            if(fechaGuia.year == today.year and fechaGuia.month == today.month):
                total += listaRecorrer[i]["monto"]
                
    return text