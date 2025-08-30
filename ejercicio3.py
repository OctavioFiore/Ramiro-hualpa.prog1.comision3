"""🔹 Ejercicio 3 — Simulador de cajero automático
El sistema debe administrar retiros de dinero de un cajero.
1.	Pedir:
o	Nombre del usuario
o	PIN (validación con 3 intentos máximos)
o	Saldo inicial (definido en el sistema, por ejemplo $50.000).
2.	Luego, permitir retiro de dinero bajo condiciones:
o	El monto debe ser múltiplo de 1000.
o	No puede superar el saldo disponible.
o	Si el retiro supera los $20.000 → cobrar una comisión del 2%.
o	El usuario puede cancelar en cualquier momento escribiendo "cancelar".
3.	Mostrar saldo actualizado.
"""

from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys

pedir_texto("Ingrese su nombre")