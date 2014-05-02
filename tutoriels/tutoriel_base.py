#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tutoriel python pour le club informatique

blabla
expliquer les deux premiers #
les commentaires se font avec #
les docstring sont différents, voir plus loin
"""
# Suit ici des informations relatives au script. Cela permet d'inclure ces
# informations automatiquement dans les modules lors de la génération automatique
# de la documentation et lors de l'exécution du code. Il n'est absolument pas
# nécessaire d'inclure cela au début des fichiers, mais comme on en parle
# rarement j'ai préféré vous montrer.
__authors__ = "Xavier Bouthillier"
__copyright__ = "Copyright 2014, Universite de Montreal"
__credits__ = ["Xavier Bouthillier"]
__license__ = "3-clause BSD"
__maintainer__ = "Xavier Bouthilier"
__email__ = "xavier.bouthillier[at]umontreal.ca"

###############################################################################
### 1. Introduction                                                         ###
###############################################################################

print "Hello World!"

# todo: Expliquer comment exécuter sur wing101

###############################################################################
### 2. Les types et variables                                               ###
###############################################################################

# Le type booléen 
print True, type(True)

# Le type entier
print 0, type(0)

# Le type double
print 0., type(0.)

# Le type string
print "une chaîne de caractères", type("une chaîne de caractères")
print 'avec guillement double ou non', type('avec guillement double ou non')

# L'object None
print None

# Déclaration de variables
ma_variable = 0

# pas besoin de faire 
# <type> <nom de variable> = <variable>
# tel que 
# int ma_variable = 0

# et on peut changer le type d'une variable
ma_variable = 0
print ma_variable, type(ma_variable)
ma_variable = "maintenant une chaîne de caractère"
print ma_variable, type(ma_variable)

# Les nom de variable ne doivent pas commencer par un chiffre, ne doivent pas
# contenir un caractère spécial (ex: @, /, é, etc) et ne doivent pas être un
# mot clé de python (ex: for, def, class, etc)

# Exécutez une ligne à la fois avec wing101 pour voir les erreurs lancées
# lorsque les noms de variables sont invalides.
nom_valide = 0
nom_valide2 = 0
2nom_invalide = 0
énom_invalide = 0
class = 0

###############################################################################
### 3. Les opérateurs et les prioprités d'opérateurs                        ###
###############################################################################

# Il y a bien sur l'addition, la soustraction, la multiplication et la division

print "1 + 1 =", 1 + 1
print "1 - 1 =", 1 - 1
print "2 * 1 =", 2 * 1
print "4 / 2 =", 4 / 2

# La division est entière en python2.+ et exacte en python3.+

print "5 / 2 =", 5 / 2
print "5 / 2. =", 5 / 2.
print "5 / 2. =", 5 / float(2)

# Il y a aussi le modulo, c'est à dire le reste d'une division

print "5 % 2 =", 5 % 2

# L'exposant 

print "5**2 =", 5**2

# On peut incrémenter la valeur d'une variable

a = 2 
print "a =", a
a += 1
print "a =",a

# Et le même s'applique pour les opérateurs -=, *= et /=




###############################################################################
### 4. Les conditions                                                       ###
###############################################################################

##############################################################################
### 5. Les listes et les tuples                                            ###
##############################################################################

##############################################################################
### 6. Les boucles                                                         ###
##############################################################################

##############################################################################
### 7. Les dictionnaires                                                   ###
##############################################################################

##############################################################################
### 8. Les fonctions                                                       ###
##############################################################################

##############################################################################
### 9. Les exceptions                                                      ###
##############################################################################

##############################################################################
### 10. Les exceptions                                                     ###
##############################################################################

##############################################################################
### 11. Les fichiers                                                       ###
##############################################################################

##############################################################################
### 12. Les classes                                                        ###
##############################################################################

##############################################################################
### 13. Les modules ?                                                      ###
##############################################################################

##############################################################################
### 14.                                                                    ###
##############################################################################
