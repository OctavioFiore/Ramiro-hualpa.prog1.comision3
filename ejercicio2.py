"""🔹 Ejercicio 2 — Sistema de calificaciones con promoción
Se desea determinar el estado académico de un alumno en base a 3 notas parciales.
1.	Pedir: nombre, legajo, y las 3 notas (enteros entre 0 y 10).
2.	Cálculo: promedio.
3.	Condiciones:
o	Si alguna nota < 4 → Desaprobado directo.
o	Si promedio < 6 → Desaprobado.
o	Si promedio entre 6 y 7 → Aprobado con final.
o	Si promedio ≥ 8 → Promocionado.
4.	Mostrar resultados con colores y estado académico final.
"""

from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys
nombre = pedir_texto("Ingrese su nombre: ")

legajo = pedir_entero("Ingrese su legajo: ")

nota1 = pedir_entero("Ingrese su primera nota(enteros entre 0 y 10): ")

nota2 = pedir_entero("Ingrese su segunda nota(enteros entre 0 y 10): ")

nota3 = pedir_entero("Ingrese su tercera nota(enteros entre 0 y 10): ")

promedio = nota1 + nota2 + nota3 / 3


if nota1 < 4 or nota2 < 4 or nota3 < 4:

    estado_academico = (Fore.RED + Style.BRIGHT + "Desaprobado directo" + Style.RESET_ALL)

if promedio < 6:
    estado_academico =(Fore.RED + Style.BRIGHT + "DesaprobadoO" + Style.RESET_ALL)
elif promedio >= 6 and promedio <= 7:

    estado_academico =(Fore.YELLOW + Style.BRIGHT + "Aprobado con final" + Style.RESET_ALL) 
elif promedio >= 8:
    estado_academico =(Fore.GREEN + Style.BRIGHT +"Promocionado"  + Style.RESET_ALL)


info("-----Estado académico final-----")

print(
    f'Nombre: {nombre}\n'
    f'Legajo: {legajo}\n'
    f'Estado academico: {estado_academico}'
)











