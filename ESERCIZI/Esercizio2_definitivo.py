#
# File: Esercizio1_definito.py
#
# Author: Felicia Proietti
#
# Date: 2026/03/17
#
# Version: 1.0
#
# Description: Esercizio 2 - laboratorio di programmazione python.
#

testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#Esercizio 2.1: Contate le righe non vuote che compongono l’estratto

#divido il testo in base al carattere \n
lista_righe = testo.split('\n')

contatore = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore = contatore + 1
#oppure if len(riga)=0

print(contatore)


########

#Esercirzio 2.2: 

lista_parole = testo.split()
counter= 0

for parola in lista_parole:
    if len(parola)>0:
        counter = counter + 1
print(counter)

testo_lista = list(testo)
print(testo_lista)

#carattere = 'a'
#alfanumerici = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#carattere in alfanumerici

