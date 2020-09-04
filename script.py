#!/usr/bin/python3

####Preámbulo
import csv, sys
import pyexcel as pe

if sys.argv[1] == "--help":
    print('\033[1mDescripción:\033[0m\n Este script clasifica los mensajes de un archivo (ejemplo del día 18 de agosto: "path-to-file/1808") a una columna en formato .csv (returns1808) para su posterior análisis.\n')
    print('\033[1mEjemplo de uso:\033[0m\n\t python script.py 18 08 [--show]\n')
    print('\033[1mArgumento opcional #3: --show\033[0m\t Esta opción fuerza al programa a mostrar siempre todos los correos "sospechosos", a revisar. De no estar presente, si hubiera más de 10 este output se suprimiría.\n')
    exit()

####Definiciones iniciales
okkeys = ["No se han seleccionando paquetes para ser actualizados","No packages marked for update", "¡Listo!", "Complete!"]
#el primer mensaje de error tiene una errata, sí.

num_to_month = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}

month = num_to_month[sys.argv[2]]

todaycolumn = int(sys.argv[1])

xlsx_file = "/home/goznalo/CCC/TareasFluor/Updates-2020.ods"
sheet = pe.get_book(file_name=xlsx_file)[month]
arrayeet = sheet.get_array()

listservers = []
for i in range(1,len(arrayeet)-3): #quitar las filas extra añadidas.
    listservers.append(arrayeet[i][0].lower())

numservers = len(listservers)
okxlist = ['x'] * numservers


#asegurarse de haber escogido bien los servidores:
if not numservers == 677 or not listservers[0] == "abedul.ccc.uam.es" or not listservers[-1] == "zeus.ccc.uam.es":
    raise ValueError('Algo ha salido mal... la lista de servidores no es correcta.')
    
nomsglist = []
for i in range(1,len(arrayeet)-3):
    nomsglist.append(False if not arrayeet[i][1] else True) #coger los espacios en blanco del día anterior

numservers = len(listservers)
okxlist = ['x'] * numservers

okxlist =  [a * b for a, b in zip(okxlist,nomsglist)]


####Extraer la información de los correos
directorio = "/home/goznalo/.thunderbird/ceesvdh2.default/Mail/fluor.ccc.uam-1.es/YUMtotal.sbd/"
archivo = sys.argv[1] + sys.argv[2] #modificar con el archivo pertinente

path = directorio + archivo

with open(path, 'r', encoding='iso-8859-1') as file3:
    messages = file3.read().replace('\n', '')
messlist = messages.split("From -")[1:]


errlist = []
falseerrcheck = []
for mess in messlist:
    sender = mess.split("<root@")[1].split(">Received:")[0]
    num = listservers.index(sender)
    for oks in okkeys:
        err = 0
        if oks in mess:
            okxlist[num] = "ok"
            falseerrcheck.append(sender)
            break
        else:
            err = 1
    if err == 1:
        errlist.append(sender)

realerrors = list(sorted(set(errlist)-set(falseerrcheck)))
        
####Escribir la información de los correos en .csv
with open(f'returns{sys.argv[1] + sys.argv[2]}.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for val in okxlist:
        writer.writerow([val])

        
####Sacar por pantalla los correos a revisar

def outputservers(yn):
    if yn:
        for err in realerrors:
            print("\t" + str(err))
    else:
        print('Demasiados servidores por mostrar (' + str(len(realerrors)) + '). Para verlos, repetir el comando con "--show" como tercer argumento')
        
print("\033[1mCorreos a revisar:\033[0m")
try:
    sys.argv[3]
    if sys.argv[3] == "--show" or len(realerrors) < 10:
        outputservers(True)
    else:
        outputservers(False)
except:
    if len(realerrors) < 10:
        outputservers(True)
    else:
        outputservers(False)
    

