#!/usr/bin/python3

import csv, sys

if sys.argv[1] == "--help":
    print('\033[1mDescripción:\033[0m\n Este script clasifica los mensajes de un archivo ("prueba1") a una columna en formato .csv (return) para su posterior análisis.\n')
    print('\033[1mEjemplo de uso:\033[0m\n\t python script.py prueba1 return')
    exit()

okkeys = ["No se han seleccionado paquetes para ser actualizados", "No packages marked for update", "¡Listo!", "Complete!"]

#modificar ./servernames.csv con el archivo pertinente
with open("/home/goznalo/CCC/servernames.csv", encoding='utf-8-sig') as file1:
    listservers =  [server.replace('\n', '') for server in file1]

numservers = len(listservers)
okxlist = ['x'] * numservers

#modificar ./nomessages.csv con el archivo pertinente
with open("/home/goznalo/CCC/nomessages.csv", encoding='utf-8-sig') as file2:
    nomsglist =  [False if not server.replace('\n', '') else True for server in file2]

okxlist =  [a * b for a, b in zip(okxlist, nomsglist)]

directorio = "/home/goznalo/.thunderbird/ceesvdh2.default/Mail/fluor.ccc.uam-1.es/"
archivo = sys.argv[1] #modificar con el archivo pertinente

path = directorio + archivo

with open(path, 'r', encoding='iso-8859-1') as file3:
    messages = file3.read().replace('\n', '')

messlist = messages.split("From -")[1:]

for mess in messlist:
    sender = mess.split("<root@")[1].split(">Received:")[0]
    num = listservers.index(sender)
    #print(listservers[num])
    for oks in okkeys:
        if oks in mess:
            okxlist[num] = "ok"
            break

with open(f'{sys.argv[2]}.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for val in okxlist:
        writer.writerow([val])

print("Hecho!")
