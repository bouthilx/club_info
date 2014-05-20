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

# On peut assigner plusieurs variable en même temps

a, b, c, d = 1, 2, 3, 4

# ou encore

a, b, c, d = (1, 2, 3, 4)

# mais pas

a, b, c, d = (1, 2, 3)

# car il faut autant de variables que de valeurs à assigner

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

# Et le même s'applique pour les opérateurs -=, *=, /=, %= et **=

# Finalement les opérateurs relationels et logiques

print 2 > 1, 2 < 1
print 2 >= 1, 2 <= 1, 2 >= 2
print 2 == 1, 2 == 2
print 2 != 1, 2 != 2

# Les priorité d'opérateurs
# 1. ( )    (tout ce qu'il y a entre les parenthèses est calculé en premier)
# 2. **     (exponentiation)
# 3. *, /, %, //
# 4. +, -
# 5. operateurs relationels: <, >, <=, >=, !=, ==
# 6. not logique
# 7. and et or logique

print 1 + 2 * 3 + 6 / 2. - 3, 
print "=", 1 + (2 * 3) + (6 / 2.) - 3
print "!=", (1 + 2) * 3 + 6 / (2. - 3)
print (2 + 4)** 3 * (4 - 5) / 4. + 5,
print "=", ((2 + 4)** 3) * ((4 - 5) / 4.) + 5
print "!=", (2 + 4** 3) * (4 - 5) / 4.) + 5

# Les opérateurs logiques

print not True
print not False and True, not (False and True)
print False and True or True, True and (False or True)

# Si une condition est vrai dans un or, l'éxécution s'arrête et renvoie True

# Par exemple, l'éxécution suivante soulève une erreur.
print 1+"string"
# Pourtant il n'y a pas d'erreur l'éxécution suivante. C'est parce que le code 
# à droite du or n'est pas éxécuté puisque le "or" est déjà vrai à droite.
print True or 1+"string"

# De la même manière, dès qu'une valeur est fausse dans un and, l'éxécution
# s'arrête et retourne False
print False and 1+"string"


###############################################################################
### 4. Les conditions                                                       ###
###############################################################################

a = 2
b = 1

if a > b: 
    print "a est plus grand que b"
elif a == b:
    print "a est égale à b"
else:
    print "a est plus petit que b"

# Le bloc d'éxécution est défini pas l'indentation du code

if a > b: # condition
    # début du bloc
    print "a est plus grand que b"
    print "une autre ligne dans le bloc"
    # fin du bloc

# c'est l'équivalent de 
# if( a > b )
# {
#     # début du bloc
#     print "a est plus grand que b"
#     print "une autre ligne dans le bloc"
#     # fin du bloc
# }

# Et on peut bien sûr imbriquer les conditions

c = 3

if a > b: 
    print "a est plus grand que b",

    if a > c:
        print "et plus grand que c"
    elif a == c:
        print "et égale à c"
    else:
        print "et plus quand que c"

elif a == b:
    print "a est égale à b"

    if a > c:
        print "et plus grand que c"
    elif a == c:
        print "et égale à c"
    else:
        print "et plus quand que c"

else:
    print "a est plus petit que b"

    if a > c:
        print "et plus grand que c"
    elif a == c:
        print "et égale à c"
    else:
        print "et plus quand que c"

# On peut aussi mettre autant de elif qu'on veut

if a > b and a > c: 
    print "a est plus grand que b et que c",
elif a > b and a == c:
    print "a est plus grand que b et est égale à c",
elif a > b and a < c:
    print "a est plus grand que b et est plus petit que c",

# etc 
else: 
    print "a est plus petit que b et c"

##############################################################################
### 5. Les listes                                                          ###
##############################################################################

l = [0, 1, 2, 3, 4]

print l[0]
print l[1]
print l[2]

print l

l[0] = 1

print l

# Les listes peuvent contenir différents types sans problèmes

l = [False, 1, 2., "Trois", None]

print l

# On peut ajouter ou enlever des éléments

l.append("nouveau")

print l

premier = l.pop()

print premier
print l

# On peut aussi supprimer un élément à un index en particulier

print l
del l[1]
print l

# obtenir l'index auquel il se trouve

print l.index(2.)

# mais attention, si votre liste contient des objets,
# deux objets différents avec exactement les même attribues 
# seront considéré comme différents si la fonction __egal__
# n'est pas redéfini (voir les section **** et ****)

# On peut additionner des listes

print [1, 2, 3, 4] + [4, 5, 6]

# On peut aussi accèder à un sous-ensemble de la liste grâce aux opérateurs ::

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print l[0]
print "l[:4] =", l[:4]
print "l[4:8] =", l[4:8]
print "l[::2] =", l[::2]

# On peut donc facilement renverser une liste

print "l[::-1] =", l[::-1]

# Mais une façon plus commune et facile à comprendre de tous

print "reversed(l) = ", list(reversed(l))

# La fonction reversed renvoie un itérateur, il faut donc convertir 
# l'itérateur en liste grace à la fonction list()

##############################################################################
### 6. Les chaînes de caractères                                           ###
##############################################################################


##############################################################################
### 7. Les tuples                                                          ###
##############################################################################

# Les tuples sont beaucoup moins utilisés que les listes, mais reste très 
# utiles car contrairement à ces dernières, ils sont immuables. C'est-à-dire
# qu'ils ne peuvent pas être modifiés.

# Le tuple se construit avec des parenthèses

t = (1, 2, 3, 4)

print t

# On peut changer une liste en tuple

t = tuple(range(10))

print t

# Il peut contenir différents types comme la liste

t = (False, 1, 2., "Trois", None)

print t

# Cependant, il n'a pas de méthodes tel que append ou pop, car on ne peut pas
# le modifier!

# On peut additionner des tuples par contre, car cela résulte en un nouveau
# tuple. Ça ne pose donc pas problème.

print (1, 2, 3, 4) + (4, 5, 6)

# Il faut comprendre que dans le code qui suit, le tuple n'est pas modifié,
# la variable t1 pointe simplement vers une nouveau tuple.

t1 = (1, 2, 3, 4)
t2 = (4, 5, 6)

t1 = t1 + t2
print t1

# Toutes les règles d'indexage des listes d'appliquent aussi au tuples

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print t.index(2)
print "t[:4] =", t[:4]
print "t[4:8] =", t[4:8]
print "t[::2] =", t[::2]
print "t[::-1] =", t[::-1]
print "reversed(t) = ", tuple(reversed(t))

##############################################################################
### 8. Les boucles                                                         ###
##############################################################################

n = 10
i = 0
while i < n:
    print i
    i += 1

for i in range(n):
    print i

n = 10
i = 0
while True:
    if i >= n:
        break
    i += 1

for i in range(n):
    if i < 5:
        continue
    if i > 5:
        break

l = [1., True, False, "quatre"]

for item in l:
    print item

for i, item in enumerate(l):
    print i, item

l2 = ["un", "deux", "trois", "quatre", "cinq"]

for item1, item2 in zip(l, l2[:4]): # changez 4 pour 3 ou 5
    print item1, item2

##############################################################################
### 9. Les dictionnaires                                                   ###
##############################################################################

d = {"un": 1, "deux": 2}
d = dict(un=1, deux=2)

d.keys()
d.values()
d.items()

del d[]

d.update()

for key, val in d.items():
    print key, val

##############################################################################
### 10. Les fonctions                                                      ###
##############################################################################

def ma_fonction():
    print "J'appelle ma fonction! :D"

ma_fonction()

a = ma_fonction()

print a

def ma_fonction():
    return 1.  

a = ma_fonction()
print a

def ma_fonction(a, b, c):
    return a, b, c

a = ma_fonction(1, 2, 3)
print a, type(a)

def ma_fonction(a, b, c=1):
    return a, b, c

print ma_fonction(1, 2, 3)
print ma_fonction(1, 2)
print ma_fonction(a=1, b=2, c=3)
print ma_fonction(b=2, a=1, c=3)
# Tout les arguments à la suite du premier mots-clé doivent
# aussi être des mots-clés
print ma_fonction(a=1, 2, c=3)
print ma_fonction(1, b=2, c=3)

# tutoriel avancé 
# ma_fonction(a, b, c=[]) danger, prendre des immuables seulement!
# ma_fonction(*liste, **dictionnaire)
# lambda

##############################################################################
### 11. Les exceptions                                                     ###
##############################################################################

try:
    # do something
except:
    # do something else otherwise

try:
    # do something
except BaseException as e:
    print str(e)

try:
    # do something
except:
    # do something else otherwise
finally:
    # do this anyway

try:
    # do something
except ValueError as e:
    # do something
except BaseException as e:
    # do something
except:
    # do something
finally:
    # do this anyway

##############################################################################
### 12. Les fichiers                                                       ###
##############################################################################

f = open("mon_fichier.txt","w")
f.write("une ligne\n")
f.write("une autre\n")
f.write("et pis une autre\n")
print f.closed
f.close()
print f.closed


def imprimer_fichier(nom_de_fichier):
    
    f2 = open(nom_de_fichier,"r") 
    for ligne in f2.readlines():
        print ligne
    
    f2.close()


imprimer_fichier("mon_fichier.txt")

f = open("mon_fichier.txt", "a")
f.write("une autre ligne à la fin\n")
f.close()

imprimer_fichier("mon_fichier.txt")

f = open("mon_fichier.txt", "w")
f.write("une autre ligne à la fin?\n")
f.close()

imprimer_fichier("mon_fichier.txt")
# Oops! Le fichier à été écrasé

with open("mon_fichier.txt", 'w') as f:
    f.write("un peu de texte\n")
    raise ValueError("Une erreur avec le fichier!")

print f.closed

import os

# Créer un dossier
os.path.mkdir     # Pour créer un seul nouveau dossier
os.path.makedirs  # Pour créer plusieurs dossier en même temps
                  # (Dans le même chemin) 
                  # ex: nouveau_dossier_racine/nouveau_dossier_enfant
                  # Tous les deux créés en même temps

# Voir si un fichier ou un dossier existe
print os.path.exists("mon_fichier.txt")
# Voir si un dossier existe
print os.path.isdir("mon_fichier.txt")
print os.path.isdir("tutoriel_avance")
print os.path.isdir("dossier_inexistant")

# Pour voir les fichiers et sous-dossier
help(os.path.walk)

#
# Chemin absolu
#

# Windows
print os.path.exists("C:/program")

# Unix (Mac et linux)
print os.path.exists("/home/usager/Documents")

#
# Chemin relatif
#

# Tous
print os.path.exists("tutoriel_avance/script.py")

# Pour être certain de ne pas se tromper avec /
print os.path.exists(os.path.join("club_info", "tutoriels", 
                                  "tutoriel_avance", "script.py"))

##############################################################################
### 13. Les classes                                                        ###
##############################################################################

class MaClasse(object):
    """
        Documentation de MaClasse
    """

    def __init__(self):
        """
            Documentation du constructeur
        """

        print "Object de MaClasse construit"
       
    def ma_methode(self):
        """
            Documentation de ma_methode
        """

        print "appel de ma_methode"

monObjet = MaClasse()
monObject.ma_methode()
print type(monObjet)
help(monObjet)

class Date(object):
    """
    """
    
    def __init__(self, year, month, day):
        """
        """

        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """
        """

        # format???
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    def __repr__(self):
        """
        """

        return str(self)

print Date(2014, 5, 25)

class Datetime(Date):
    """
    """

    def __init__(self, year, month, day, hour, minute, second):
        super(Datetime, self).__init__(year, month, day)

        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """
        """

        date = super(Datetime, self).__str__()
    
        date += " " + str(self.hour)
        date += ":" + str(self.minute)
        date += ":" + str(self.second)

        return date

print Datetime(2014, 5, 25, 14, 5, 44)

class DatetimeAMPM(Date):
    """
    """

    def isAM(self):
        """
        """

        return self.hour < 12

    def isPM(self):
        """
        """

        return not self.isAM()

    def get_hour(self):
        """
        """

        return self.hour % 12
    
    def __str__(self):
        """
        """

        date = super(Datetime, self).__str__()

        if self.hour < 12:
            date += " AM "
        else:
            date += " PM "
        
        date += str(self.hour % 12)
        date += ":" + str(self.minute)
        date += ":" + str(self.second)

        return date


datetime = DatetimeAMPM(2014, 5, 25, 14, 5, 44)
print datetime
print datetime.isAM()

# Voir dans tutoriel avancé pour l'interface getter/setter

##############################################################################
### 14. Les modules                                                        ###
##############################################################################
