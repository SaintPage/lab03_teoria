"""
Programa principal del Problema 1 (Laboratorio 3).

Reutiliza integramente el shunting_yard.py del laboratorio anterior:
tokenizar -> insertar_concatenacion -> shunting_yard -> expandir_extensiones.
Con el postfix ya expandido (sin + ni ?) se construye el arbol sintactico y
se dibuja en un PNG.

Uso:
    python3 main.py [archivo.txt]
"""

import sys

from shunting_yard import (tokenizar, insertar_concatenacion, shunting_yard,
                            expandir_extensiones)
from arbol_sintactico import construir_arbol, dibujar_arbol, recorrido_preorden


def procesar(numero, expresion):
    print(f'[{numero}] Expresion: {expresion}')

    tokens, error = tokenizar(expresion)
    if error is not None:
        print(f'    ERROR (tokenizando): {error}\n')
        return

    tokens_concat = insertar_concatenacion(tokens)
    print('    Con concatenacion:', ''.join(t.texto for t in tokens_concat))

    postfix, pasos, error = shunting_yard(tokens_concat)
    if error is not None:
        print(f'    ERROR (shunting yard): {error}\n')
        return
    print('    Postfix           :', ' '.join(postfix))

    expandida, cambios = expandir_extensiones(postfix)
    if cambios:
        print('    Extensiones expandidas:')
        for c in cambios:
            print('       -', c)
    print('    Postfix expandido :', ' '.join(expandida))

    raiz = construir_arbol(expandida)
    print('    Arbol             :', recorrido_preorden(raiz))

    nombre = f'arbol_{numero}'
    ruta = dibujar_arbol(raiz, nombre)
    print('    Imagen            :', ruta)
    print()


def main():
    archivo = sys.argv[1] if len(sys.argv) > 1 else 'expresiones.txt'
    with open(archivo, encoding='utf-8') as f:
        lineas = [ln.rstrip('\n').rstrip('\r') for ln in f]
        lineas = [ln for ln in lineas if ln.strip() and not ln.lstrip().startswith('//')]

    for i, expresion in enumerate(lineas, start=1):
        procesar(i, expresion)


if __name__ == '__main__':
    main()
