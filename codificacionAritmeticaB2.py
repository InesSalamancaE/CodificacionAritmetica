# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:45:50 2024

@author: Inespelirroja
"""

def binary_arithmetic_coding(L, H):
    code = ""

    while True:
        # Multiplicamos por 2 el intervalo H
        H *= 2
        # Multiplicamos por 2 el intervalo L
        L *= 2

        # Verificamos si el primer bit del entero de H es 1
        if int(H) == 1:
            code += '1'
            break
        else:
            # Verificamos si el primer bit del entero de L es 1
            if int(L) == 1:
                code += '0'
                break
            else:
                # Si no hay coincidencia, seguimos buscando
                code += '1' if H >= 1 else '0'

    return code

# Ejemplo de uso
L = 1/5
H = 3/10

binary_code = binary_arithmetic_coding(L, H)
print("Codificación binaria:", binary_code)

# Ejemplo de uso
L = 93/343
H = 97/343

binary_code = binary_arithmetic_coding(L, H)
print("Codificación binaria:", binary_code)
