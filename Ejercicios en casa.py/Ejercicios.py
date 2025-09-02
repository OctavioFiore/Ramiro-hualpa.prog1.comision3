"""🔹 Ejercicio 1 — Clasificación de impuestos
El programa debe calcular el impuesto anual que debe pagar una persona en función de sus ingresos y edad:
1.	Pedir:
o	Nombre completo
o	Edad
o	Ingresos anuales
2.	Reglas:
o	Si ingresos < $500.000 → No paga impuestos.
o	Si ingresos ≥ $500.000 y < $2.000.000 → paga 10%.
o	Si ingresos ≥ $2.000.000 y < $5.000.000 → paga 20%.
o	Si ingresos ≥ $5.000.000 → paga 35%.
o	Si la persona tiene más de 65 años, el impuesto se reduce en un 50%.
3.	Salida clara con nombre, ingresos, edad e impuesto final."""

from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys


nombre_completo = pedir_texto("Ingrese su nombre completo: ")
edad = pedir_entero("Ingrese su edad: ")
ingresos_anuales = pedir_float("Ingresos anuales: ")


if ingresos_anuales < 500000:
    impuesto_final = 0
elif ingresos_anuales < 2000000:
    impuesto_final = ingresos_anuales * 0.10
elif ingresos_anuales < 5000000:
    impuesto_final = ingresos_anuales * 0.20
else:
    impuesto_final = ingresos_anuales * 0.35


if edad > 65:
    impuesto_final /= 2


print(
    f'Nombre: {nombre_completo}\n'
    f'Ingresos anuales: {ingresos_anuales:,.2f}\n'
    f'Edad: {edad}\n'
    f'Impuesto final: {impuesto_final:,.2f}'
)



















