# Thunderbird to .csv

## Introducción
Cada día llegan miles de emails procedentes de las máquinas del CCC-UAM al servidor de correo. Cada uno está programado con un fin específico. En concreto, hay unos ~300 correos que llegan a diario de las máquinas, producto del crontab de cada una de ellas, en el que se establece una ejecución diaria (y en algunos casos a ciertas horas) de `yum update`, para mantener el software al día. 

## Objetivo
Los correos diarios de `yum update` han de ser clasificados en una hoja de cálculo, en base a 
1. No ha llegado un correo de una máquina -> escribir "x" en la casilla correspondiente a la fila de la máquina y la columna del día
2. Sí ha llegado un correo de una máquina:
    1. El correo contiene un mensaje de error a la hora del update -> escribir "x"
    2. El correo contiene un "Listo!", "No packages marked for an update", o "No ha seleccionado paquetes para la actualización" -> escribir "ok"
    
Esta tarea acaba siendo bastante repetitiva y monótona, aun con trucos como ordenar los emails. ¿Y a quién se le dan bien las tareas monótonas y repetitivas? A los ordenadores. Por tanto vamos a implementar un programilla para automatizar este proceso.

## Requisitos previos

### Software
* Python 3.x, junto con los módulos csv y pyexcel.
* Thunderbird. Evidentemente.
* Procesador de hojas de cálculo: La hoja de cálculo usada como input está en formato .ods, por tanto es preferible tener instalado LibreOffice/OpenOffice Calc, o Microsoft Excel con la extensión apropiada. Otras alternativas (como Softmaker Planmaker) pueden no soportar este formato.

### Estructura de los directorios
* Mensajes de Thunderbird: Estos han de ser localizados inicialmente en el ordenador de cada uno. En mi caso están rebuscando en el directorio `.thunderbird`, encontrados rebuscando un poco. 
* Hoja de cálculo de origen: ver disclaimer al final.


## Uso 
Se recomienda el uso del ejecutable script.py, mediante línea de comandos. El script requiere dos argumento posicionales, siendo el primero de estos el día del mes del que se quiere el procesamiento, y el segundo el mes en formato numérico de dos dígitos (mm). Ejemplo:

`python script.py 18 08 [--show]`

La ejecución acaba mostrando por pantalla aquellos servidores cuyos mensajes son posibles errores. Este output es suprimido por el programa en el caso de ser demasiado grande (> 10 servidores), junto con un mensaje avisando de ello. Para forzar la salida del output es necesario usar "--show" como tercer argumento posicional.

## Contenido
El repositorio es muy simple: contiene el presente README, el archivo .csv resultante, un Jupyter Notebook con el programa detallado paso a paso, y finalmente un ejecutable de Python para realizar la tarea de forma automática a través de la shell.

### Disclaimer: archivos necesarios
Por temas de privacidad del CCC-UAM, no es posible mostrar la información de los servidores (por ejemplo sus nombres), por tanto tanto los mensajes como la lista con servidores serán archivos ajenos al repositorio, llamados por el programa solo localmente. En cualquier caso, no es difícil adaptar el programa para usarlo en el ordenador de cada uno, con sus respectivos mensajes y servidores.
