# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:48:07 2024

@author: Inespelirroja
"""
def vigenere_clasico(mensaje_cifrado, clave, alfabeto):
    mensaje_original = ""
    n = len(alfabeto)
    espacio_contador = 0

    for i, letra in enumerate(mensaje_cifrado):
        if letra in alfabeto:
            # Obtener la posición de la letra en el alfabeto
            pos_letra = alfabeto.index(letra)
            # Obtener la posición de la letra de la clave en el alfabeto
            pos_clave = alfabeto.index(clave[i % len(clave)])
            # Calcular la posición de la letra original
            pos_original = (pos_letra - pos_clave) % n
            # Obtener la letra original
            letra_original = alfabeto[pos_original]
            mensaje_original += letra_original
            espacio_contador = 0
        elif letra == " ":
            espacio_contador += 1
            mensaje_original += letra
            if espacio_contador == 2:
                mensaje_original += "\n"
                espacio_contador = 0
        else:
            mensaje_original += letra
    
    return mensaje_original

def main():
    alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ0123456789 ,.:!-¿?()"
    clave_K1 = "UCBxHcl!6jñydiFoMB!vol!:da"
    #CLAVE CIFRADO 2 (K_2) "ÑaKtfDaZ2F77DU8ExqtUVdñQmzw1úF"
    clave_k2 = "ÑaKtfDaZ2F77DU8ExqtUVdñQmzw1úF"
    mensaje_cifrado = "cCTñScE((ÚHGfiXfúPhmqzgi:uÍCrzVtCc vHC:lJfMHovhb4xAi3VFKxfsp AGyv(YsáSWvHb¿iopÁKDxKcD5ÉnGofpJGÁP5mfA(lr ÁCrIhis¿6)o-vpHoCFnmAFs3veÍEJIRcd4pneGjCFzCrgKrz4kxeLGMñHiF!ÉñySBmvrPT?zfFh3ñuáCSñLnop6mCo:oFqTB4KICj3oá3sCxPqbñbuñLgwvzMr?DHE!gfiUsN!Z.njeCñp:(X8WP4CoJ4ñpaLEPOYkohgneKdBJAjUcxod43: Sk8mr:bB6AIIl(7JóBevAs53NiÚVPño,-35"
    mensaje_cifrado_2 = "aeWMfPd4íJaÍH3duBJNUMpCSsDñéÉTé5K2ÓtjIYVñp!VS9ópUT5Gúr4vcOwxdna!ó0UÁÑÚQ Í1 ACú4EmARh(VWxt6t23!SL14Oú NG-rt¿Áe4aA0YjeÓÍiTLóuñÍV¿i7S7z4KCÍEDÍLcPL9qpÍYxIz7Ó35í5JLs45-FFy-xÍ2:5O(V:Ú.,NAmxFlN(1F!klv:HbmLWRGaCk!1Ú87:YYD7HmGxGJh(qwsYÓ3-yDiUIñaPI¿E-0hJWzñx.ZrJÓ.QUOxVhú2jGzu buoEy!I3f10?eaCáñ.SHUFNCsAFJQaiwZlHS:qf8xcÉÁI(X¿22lÉKFÓÍaztñyS0PZ suxé(f0CÉhb(7Óxw,bóT5BorRQFVQQAHeÑ:o7ÑtyG,9gHEÚkO,uÍkÚéYI)8dyáG)-KR)Ú:pr5!JéBpAIOHFxNeaqSQr5Ñ"

    mensaje_original = vigenere_clasico(mensaje_cifrado, clave_K1, alfabeto)
    print("Mensaje original:")
    print(mensaje_original)
    
    mensaje_original = vigenere_clasico(mensaje_cifrado_2, clave_k2, alfabeto)
    print("Mensaje original:")
    print(mensaje_original)

if __name__ == "__main__":
    main()
