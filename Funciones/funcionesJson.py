import json

def abrirJSONData():
    dicFinal=[]
    with open("./dataProyect/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONData(dic):
    with open("./dataProyect/datos.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJSONInfo():
    dicFinal=[]
    with open("./dataProyect/informes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONInfo(dic):
    with open("./dataProyect/informes.json",'w') as outFile:
        json.dump(dic,outFile)

