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

edad=pedir_entero("Ingrese numero entero: ")
nombre_completo=pedir_texto("Ingrese su nombre completo")
