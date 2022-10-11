#!/usr/bin/env python

import string
import sys


######################################################################################
#
#  Define varias clases que definen cada uno de los diferentes componentes lexicos
#
#
#
######################################################################################

# Clase generica que define un componente lexico 
class Componente:
    def __init__(self, linea):
        self.cat = str(self.__class__.__name__)
        self.linea = linea


# este metodo mostrará por pantalla un componente lexico
def __str__(self):
    s = []
    for k, v in self.__dict__.items():
        if k != "cat":
            s.append("%s: %s" % (k, v))
    if s:
        return "%s (%s)" % (self.cat, ", ".join(s))
    else:
        return self.cat


# definicion de las clases que representan cada uno de los componentes lexicos

# Algunas tendran campos adicionales para almacenar informacion importante (valor de un número, etc.)

# clases para los simbolos de puntuacion y operadores


class OpAsigna(Componente):
    def __init__(self, nl):
        Componente.__init__(self, nl)


# Clase que define la categoria OpAdd
class OpAdd(Componente):
    # debe almacenarse de que operador se trata
    def __init__(self, nl):
        Componente.__init__(self, nl)


# Clase que define la categoria OpMult
class OpMult(Componente):
    # Debe alnmacenarse que operador es
    def __init__(self, nl):
        Componente.__init__(self, nl)


# Clases para representar los numeros.
# Puede dividirse en 2 para representar los enteros y los reales de forma independiente
# Si se opta por una sola categoria debe almacenarse el tipo de los datos además del valor
class Numero(Componente):
    def __init__(self, v,  nl, real):
        Componente.__init__(self, nl)
        self.valor = v
        self.real = real


# clases para representar los identificadores y palabras reservadas
class Identif(Componente):
    def __init__(self, v, nl):
        Componente.__init__(self, nl)
        self.valor = v
        self.linea = nl


# Clase que representa las palabras reservadas.
# Será una clase independiente de los identificadores para facilitar el analisis sintactico
class PR(Componente):
    def __init__(self, v, nl):
        # Completar
        Componente.__init__(self, nl)
        self.v = v


# Clase que define la categoria OpRel
# Debe almacenarse que operador es concretamente

class OpRel(Componente):
    def __init__(self, v, nl):
        # Completar
        Componente.__init__(self, nl)


class EOF(Componente):
    def __init__(self, nl):
        Componente.__init__(self, nl)
