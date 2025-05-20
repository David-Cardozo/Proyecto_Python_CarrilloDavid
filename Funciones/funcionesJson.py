import json

def abrirJSON():
    dicFinal=[]
    with open("./dataProyect/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./dataProyect/datos.json",'w') as outFile:
        json.dump(dic,outFile)