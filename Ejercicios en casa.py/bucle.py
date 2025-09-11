




def valor_letras(letras):
    l1 = ord(letras[0]) - ord('A')
    l2 = ord(letras[1]) - ord('A')
    l3 = ord(letras[2]) - ord('A')
    return l1 * 26**2 + l2 * 26 + l3  

def validar_patente(patente_formato):

    patente_formato = patente_formato.strip().upper()


    if len(patente_formato) != 6 or not patente_formato[:3].isalpha() or not patente_formato[3:].isdigit():
        return 'Formato de patente inválido'

    letras = patente_formato[:3]
    numeros = patente_formato[3:]


    idx_letras = valor_letras(letras)        
    idx_num    = int(numeros)                
    numero_patente = idx_letras * 1000 + idx_num + 1  

    return f'La patente {patente_formato} es la patente número: {numero_patente}'

def validar_inverso(patente_numero):
    MAX_PATENTES = 26**3 * 1000
    n = int(patente_numero)

    if not (1 <= n <= MAX_PATENTES):
        return f'El número {patente_numero} no es una patente válida'

    n0 = n - 1
    valor_letras = n0 // 1000
    numero = n0 % 1000

    l1 = valor_letras // 26**2
    l2 = (valor_letras // 26) % 26
    l3 = valor_letras % 26

    letras = chr(ord('A') + l1) + chr(ord('A') + l2) + chr(ord('A') + l3)
    return f'La patente n°{n} es {letras}{numero:03d}'

ver_patente = int(input('Si quieres ver el número de patente ingresa 1\nSi quieres ver una patente por su número ingresa 2: '))

if ver_patente == 1:
    patente = input('Ingresa la patente (AAA111): ')
    print(validar_patente(patente))
elif ver_patente == 2:
    num = input('Ingresa el número de patente: ')
    print(validar_inverso(num))
