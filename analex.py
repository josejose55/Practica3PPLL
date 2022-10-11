#!/usr/bin/env python

import componentes
# import errores
import flujo
import string
import sys
import os
from sys import argv


class Analex:
    #############################################################################
    #  Conjunto de palabras reservadas para comprobar si un identificador es PR
    #############################################################################
    PR = frozenset(
        ["PROGRAMA", "VAR", "ENTERO", "REAL", "BOOLEANO", "INICIO", "FIN", "SI", "ENTONCES", "SINO", "MIENTRAS",
         "HACER", "LEE", "ESCRIBE", "Y", "O", "NO", "CIERTO", "FALSO"])

    ############################################################################
    #
    #  Funcion: __init__
    #  Tarea: Constructor de la clase
    #  Prametros: flujo: flujo de caracteres de entrada
    #  Devuelve: --
    #
    ############################################################################
    def __init__(self, flujo):
        self.flujo = flujo
        self.poserror = 0
        self.nlinea = 1

    ############################################################################
    #
    #  Funcion: TrataNum
    #  Tarea: Lee un número del flujo
    #  Parametros: flujo: flujo de caracteres de entrada
    #              ch: primera caracter a tratar
    #  Devuelve: El valor numerico de la cadena leida
    #
    ############################################################################
    def TrataNum(self, flujo, ch):
        l = ch
        real = False
        ch = self.flujo.siguiente()
        # Completar

        num = "0123456789"

        while ch in num and ch != "":
            l = l + ch
            ch = self.flujo.siguiente()

            if ch == ".":
                real = True
                ch = self.flujo.siguiente()

                if ch not in num:
                    self.flujo.devuelve(ch)
                    self.flujo.devuelve(".")
                    real = False
                    #return l, real
                    return componentes.Numero(l, self.nlinea, real)
                else:
                    l = l + "."

        return componentes.Numero(l, self.nlinea, real)
        #return l, real

    ############################################################################
    #
    #  Funcion: TrataIdent
    #  Tarea: Lee identificadores
    #  Prametros: flujo: flujo de caracteres de entrada
    #              ch: Primer caracter a tratar
    #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
    #
    ############################################################################
    def TrataIdent(self, flujo, ch):
        l = ch
        # Completar

        return l

    ############################################################################
    #
    #  Funcion: TrataIdent
    #  Tarea: Lee identificadores
    #  Prametros: flujo: flujo de caracteres de entrada
    #             ch: Primer caracter a tratar
    #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
    #
    ############################################################################
    def TrataComent(self, flujo):
        # Completar
        pass

    ############################################################################
    #
    #  Funcion: EliminaBlancos
    #  Tarea: Descarta todos los caracteres blancos que hay en el flujo de entrada
    #  Prametros: flujo: flujo de caracteres de entrada
    #  Devuelve: --
    #
    ############################################################################
    def EliminaBlancos(self, flujo):
        # Completar
        ch = self.flujo.siguiente()

        while ch == " ":
            ch = self.flujo.siguiente()

        self.flujo.devuelve(ch)



    ############################################################################
    #
    #  Funcion: Analiza
    #  Tarea:  Identifica los diferentes componentes lexicos
    #  Prametros:  --
    #  Devuelve: Devuelve un componente lexico
    #
    ############################################################################

    def Analiza(self):
        l = ""
        ch = self.flujo.siguiente()
        print("---",ch)
        print("tam", len(ch))
        # si se ha terminado el fichero
        if ch == "":
            return componentes.EOF(self.nlinea)
        # acciones si hemos encontrado un blanco
        if ch == " " or ch == "\t":
            print("Blanco")
            self.EliminaBlancos(self.flujo)
            return self.Analiza()
        # acciones si hemos encontrado un salto de línea
        elif ch == "\n" or ch == "\r":
            self.nlinea = self.nlinea + 1
            return self.Analiza()
        # completar aqui para todas las categorias lexicas
        elif ch == ":=":
            pass
        elif ch in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM":
            print("letra")
        elif ch in "0123456789":
            # l = l ++ self.TrataNum(self.flujo, ch)
            print("numero")
            return self.TrataNum(self.flujo, ch)
            #l, r = self.TrataNum(self.flujo, ch)
            #return componentes.Numero(l, r, self.nlinea)
        # se ha encontrado un caracter no permitido
        elif ch:
            print("ERROR LEXICO  Linea " + str(self.nlinea) + " ::  Caracter " + ch + " invalido ")
            return self.Analiza()
        else:
            # el final de fichero
            return componentes.EOF(self.nlinea)


############################################################################
#
#  Funcion: __main__
#  Tarea: Programa principal de prueba del analizador lexico
#  Prametros:  --
#  Devuelve: --
#
############################################################################

if __name__ == "__main__":
    script, filename = argv
    txt = open(filename)
    print("PROGRAMA FUENTE %r" % filename)
    i = 0
    fl = flujo.Flujo(txt)
    analex = Analex(fl)
    c = analex.Analiza()
    while c.cat != "EOF":
        print(c)
        print(c.valor)
        c = analex.Analiza()
    i = i + 1
