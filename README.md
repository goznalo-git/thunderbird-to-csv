# Thunderbird to .csv

## Introducción
Cada día llegan miles de emails procedentes de las máquinas del CCC-UAM al servidor de correo. Cada uno está programado con un fin específico. En concreto, hay unos ~300 correos que llegan a diario de las máquinas, producto del crontab de cada una de ellas, en el que se establece una ejecución diaria (y en algunos casos a ciertas horas) de `yum update`, para mantener el software al día. 

## Objetivo
Los correos diarios de `yum update` han de ser clasificados en un Excel, en base a 
1. No ha llegado un correo de una máquina -> escribir x en la casilla correspondiente a la fila de la máquina y la columna del día
2. Sí ha llegado un correo de una máquina:
    1. El correo contiene un mensaje de error a la hora del update -> escribir x
    2. El correo contiene un "Listo!", "No packages marked for an update", o "No ha seleccionado paquetes para la actualización" -> escribir ok
    
Esta tarea acaba siendo bastante repetitiva y monótona, aun con trucos como ordenar los emails. ¿Y a quién se le dan bien las tareas monótonas y repetitivas? A los ordenadores. Por tanto vamos a implementar un programilla para automatizar este proceso.

## Contenido
El repositorio es muy simple: contiene el presente README, el archivo .csv resultante, un Jupyter Notebook con el programa detallado paso a paso, y finalmente un ejecutable de Python para realizar la tarea de forma automática a través de la shell.

### Disclaimer: archivos necesarios
Por temas de privacidad del CCC-UAM, no es posible mostrar la información de los servidores (por ejemplo sus nombres), por tanto tanto los mensajes como la lista con servidores serán archivos ajenos al repositorio, llamados por el programa solo localmente. En cualquier caso, no es difícil adaptar el programa para usarlo en el ordenador de cada uno, con sus respectivos mensajes y servidores.
