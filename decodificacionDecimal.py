# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:16:15 2024

@author: Inespelirroja
"""

import decimal

class Alfabeto:
    def __init__(self, c):
        self.caracter = c
        self.frecuencia = 1
        self.L = None
        self.H = None

    def set_LH(self, L, H):
        self.L = L
        self.H = H

    def get_char(self):
        return self.caracter

    def get_frecuencia(self):
        return self.frecuencia

    def aumentar_frecuencia(self):
        self.frecuencia += 1

    def get_L(self):
        return self.L

    def get_H(self):
        return self.H


def generar_lista_alfabeto(alf):
    lista = []

    for c in alf:
        x = check_exist(lista, c)
        if x == -1:
            new_letter = Alfabeto(c)
            lista.append(new_letter)
        else:
            lista[x].aumentar_frecuencia()

    return lista


def obtener_codigo_binario(file):
    with open(file, 'r') as file:
        return file.read()


def check_exist(lst, c):
    for i, item in enumerate(lst):
        if item.get_char() == c:
            return i
    return -1


def calcular_mensaje(lon, num, lst):
    msg = []
    num_actual = num

    for _ in range(lon):
        Lj, Hj = decimal.Decimal(0), decimal.Decimal(0)

        for x, item in enumerate(lst):
            if num_actual >= item.get_L() and num_actual < item.get_H():
                Lj, Hj = item.get_L(), item.get_H()
                msg.append(str(item.get_char()))
                break

        num_actual = (num_actual - Lj) / (Hj - Lj)

    return ''.join(msg)


def get_decimal(binary):
    decimal_val = decimal.Decimal(0)
    start = -1

    for i, char in enumerate(binary):
        if char != '.':
            start += 1
        else:
            break

    for i, char in enumerate(binary):
        if char != '.':
            if char == '1':
                if start >= 0:
                    decimal_val += decimal.Decimal(2) ** start
                else:
                    decimal_val += decimal.Decimal(2) ** start
            start -= 1

    return decimal_val.quantize(decimal.Decimal(10) ** -DECIMALS, rounding=decimal.ROUND_HALF_UP)


def dividir_fuente(lst):
    total = sum(item.get_frecuencia() for item in lst)

    div = decimal.Decimal(1) / decimal.Decimal(total)
    actual_div = decimal.Decimal(0)

    for i, item in enumerate(lst):
        nxt_div = actual_div + div * decimal.Decimal(item.get_frecuencia())
        if i == len(lst) - 1:
            nxt_div = decimal.Decimal(1)
        item.set_LH(actual_div, nxt_div)
        actual_div = nxt_div


def main():
    # IMPORTAMOS EL CÓDIGO CODIFICADO EN BINARIO DE UN ARCHIVO TXT
    file_path = "binaryString.txt"
    
    # FUENTE DE INFORMACIÓN
    alfabeto = "ABCDEFGHIJKLMNÑ OPQRSTUVWXYZ"
    lista = generar_lista_alfabeto(alfabeto)
    dividir_fuente(lista)

    # NUMERO BINARIO A MENSAJE
    codificacion_binaria = obtener_codigo_binario(file_path)
    num_decimal = get_decimal(codificacion_binaria)
    longitud = 24

    mensaje_decodificado = calcular_mensaje(longitud, num_decimal, lista)
    print("El mensaje decodificado es:", mensaje_decodificado)


if __name__ == "__main__":
    DECIMALS = 200
    decimal.getcontext().prec = DECIMALS
    main()
