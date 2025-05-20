def recorrerLista (listaRecorrer):
    for i in range(len(listaRecorrer)):
        print("=========================================================================")
        print("                            Gasto N°", listaRecorrer[i]["id"])
        print("=========================================================================")
        print("- Monto de gasto:   ", listaRecorrer[i]["monto"])
        print("- Categoria de gasto:   ", listaRecorrer[i]["categoria"])
        print("- Descripcion de gasto:   ", listaRecorrer[i]["descripcion"])
        print("- Fecha de gasto:   ", listaRecorrer[i]["fecha"])
        print("=========================================================================")