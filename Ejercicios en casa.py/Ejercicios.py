
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
    f'Promedio: {promedio}\n'
    f'Estado academico: {estado_academico}'

)
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

init(autoreset=True)
pin_correcto = "1234"
max_intentos = 3
saldo_inicial = 60000

nombre_del_usuario = pedir_texto("Ingrese su nombre: ")
print(Fore.CYAN + f"Hola, {nombre_del_usuario}.")

acceso = False
intentos = 0

while intentos < max_intentos:
    pin_ingresado = input("Ingrese su PIN: ")
    if pin_ingresado == pin_correcto:
        print(Fore.GREEN + "PIN correcto. Bienvenido.")
        acceso = True
        break
    else:
        intentos += 1
        print(Fore.RED + f"PIN incorrecto. Intento {intentos} de {max_intentos}")

if not acceso:
    print(Fore.RED + "Demasiados intentos. Operación cancelada.")
    sys.exit(0)


print(Fore.YELLOW + f"Saldo disponible: ${saldo_inicial:.2f}")

while True:
    entrada = input("Ingrese el monto que quiere retirar (o 'cancelar'): ").strip().lower()

    if entrada == "cancelar":
        print(Fore.CYAN + "Operación cancelada por el usuario.")
        sys.exit(0)


    try:
        retiro = int(entrada)
    except ValueError:
        print(Fore.RED + "Debe ingresar un número válido o escribir 'cancelar'.")
        continue  


    if retiro <= 0:
        print(Fore.RED + "El retiro debe ser mayor que 0.")
        continue

    if retiro % 1000 != 0:
        print(Fore.RED + "El monto debe ser múltiplo de 1000.")
        continue


    comision = retiro * 0.02 if retiro > 20000 else 0
    monto_total = retiro + comision

    
    if monto_total > saldo_inicial:
        print(Fore.RED + "No puede superar el saldo disponible (incluida la comisión).")
        continue


    saldo_anterior = saldo_inicial
    saldo_inicial -= monto_total

    print(Fore.MAGENTA + f"Comisión aplicada (2% si corresponde): ${comision:.2f}")
    print(Fore.CYAN    + f"Total debitado: ${monto_total:.2f}")
    print(Fore.WHITE   + f"Saldo anterior: ${saldo_anterior:.2f}")
    print(Fore.GREEN   + f"Saldo actual:   ${saldo_inicial:.2f}")
    break  

"""🔹 Ejercicio 4 — Categoría de conductores
Un sistema de tránsito clasifica conductores en base a su edad y experiencia.
1.	Pedir: nombre, edad, y años de experiencia conduciendo.
2.	Condiciones:
o	Si edad < 18 → No puede conducir.
o	Si edad ≥ 18 y experiencia < 1 → Principiante.
o	Si edad ≥ 21 y experiencia entre 1 y 5 años → Conductor intermedio.
o	Si edad ≥ 30 y experiencia > 10 → Conductor profesional.
o	En cualquier otro caso → Conductor estándar.
3.	Mostrar mensaje claro al usuario.

"""



from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys

init(autoreset=True)

nombre = pedir_texto("Ingrese su nombre: ") 
edad = pedir_entero("Ingrese su edad: ")
anos_experiencia = pedir_entero("Ingrese sus años de experiencia conduciendo: ")

if edad < 18:
    nivel = Fore.RED + "No puede conducir"
elif edad >= 18 and anos_experiencia < 1:
    nivel = Fore.YELLOW + "Principiante"
elif edad >= 21 and 1 <= anos_experiencia <= 5:
    nivel = Fore.CYAN + "Conductor intermedio"
elif edad >= 30 and anos_experiencia > 10:
    nivel = Fore.GREEN + "Conductor profesional"
else:
    nivel = Fore.WHITE + "Conductor estándar"

info("----- Clasificación ----")
print(
    f"Nombre: {nombre}\n"
    f"Edad: {edad}\n"
    f"Clasificación: {nivel}"
)

"""🔹 Ejercicio 5 — Simulador de carrito de compras
El sistema simula una compra en línea.
1.	Pedir al usuario:
o	Nombre del cliente
o	Cantidad de productos (validar entero positivo)
o	Monto total de la compra (float positivo)
o	Medio de pago (efectivo, debito, credito, mercado_pago)
2.	Aplicar reglas:
o	Si medio = efectivo → 15% de descuento.
o	Si medio = debito → 10% de descuento.
o	Si medio = credito → recargo de 5%.
o	Si medio = mercado_pago → 20% de descuento, pero solo si el total > $10.000.
3.	Si el cliente compra más de 10 productos, agregar un descuento extra del 5% sobre el total final.
4.	Mostrar el importe final a pagar con detalle de todos los descuentos/recargos aplicados.
"""


from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys

init(autoreset=True)


nombre=pedir_texto("Ingrese su nombre: ")


cantidad_productos=pedir_entero("Ingrese la cantidad de producto: ")
if cantidad_productos <= 0:
    print(Fore.RED + "La cantidad de productos debe ser mayor que 0.")
    raise SystemExit

monto_total=pedir_float("Ingrese el monto total: ")

if monto_total <= 0:
    print(Fore.RED + "El monto total debe ser mayor que 0.")
    raise SystemExit

medio_pago = pedir_opcion(
    "Medio de pago (efectivo/debito/credito/mercado_pago): ",
    opciones=["efectivo", "debito", "credito", "mercado_pago"]
).strip().lower()



descuento = 0.0
recargo = 0.0
detalle_medio = ""

if medio_pago == "efectivo":
    descuento = monto_total * 0.15
    detalle_medio = "Efectivo → 15% de descuento"
elif medio_pago == "debito":
    descuento = monto_total * 0.10
    detalle_medio = "Débito → 10% de descuento"
elif medio_pago == "credito":
    recargo = monto_total * 0.05
    detalle_medio = "Crédito → 5% de recargo"
elif medio_pago == "mercado_pago":
    if monto_total > 10000:
        descuento = monto_total * 0.20
        detalle_medio = "Mercado Pago → 20% de descuento (por total > $10.000)"
    else:
        detalle_medio = "Mercado Pago → sin descuento (total ≤ $10.000)"


total_parcial = monto_total - descuento + recargo

descuento_extra = 0.0
detalle_extra = "Sin descuento extra por cantidad"
if cantidad_productos > 10:
    descuento_extra = total_parcial * 0.05  
    detalle_extra = "Descuento extra 5% por más de 10 productos"

monto_final = total_parcial - descuento_extra

info("----- Importe final ----")
print(
    f"Nombre del cliente: {nombre}\n"
    f"Cantidad de productos: {cantidad_productos}\n"
    f"Monto base: ${monto_total:.2f}\n"
    f"{detalle_medio}\n"
    f"  - Descuento medio de pago: ${descuento:.2f}\n"
    f"  + Recargo medio de pago:   ${recargo:.2f}\n"
    f"Subtotal: ${total_parcial:.2f}\n"
    f"{detalle_extra}\n"
    f"  - Descuento extra: ${descuento_extra:.2f}\n"
    f"{Fore.GREEN}TOTAL A PAGAR: ${monto_final:.2f}"
)
















