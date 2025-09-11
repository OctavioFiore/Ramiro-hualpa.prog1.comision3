
"""0) Calentamiento: strings y números
Practicá: str.isalpha(), str.isupper(), str.isdigit(), slicing s[:3], s[3:], len(s).
Reto 0:

Pedí una cadena y decí si tiene 6 chars.

Decí si los 3 primeros son letras y los 3 últimos son dígitos.
"""

def combrar_la_patente(patente):


    if len(patente)!=6:
        return "Error: la patente debe tener 6 caracteres"


    letras=patente[:3]

    numeros=patente[3:]



    if letras.isalpha() and letras.isupper() and numeros.isdigit():
        return "La patente es valida"
    else:
        return "La patente no es valida"





patente=input("Ingrese la patente: ")

casos = [
    ("ABC123", "La patente es valida"),
    ("AbC123", "La patente no es valida"),
    ("ABC12", "Error: la patente debe tener 6 caracteres"),
    ("ABC12X", "La patente no es valida"),
]

for entrada, esperado in casos:
    obtenido = combrar_la_patente(entrada)
    if obtenido == esperado:
        print(f"[OK] {entrada}")
    else:
        print(f"[FAIL] {entrada} → {obtenido} (esperado {esperado})")

numero=int(input("Ingrese un numero entero:"))


print(f'{numero:03d}')








def indice_letra(i):

    return chr(65+i)
            
            
    


