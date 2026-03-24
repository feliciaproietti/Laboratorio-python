#
# File: Esercizio1.py
#
# Author: felicia Proietti
#
# Date: 2026/03/09
#
# Version: 1.0
#
# Description: Esercio 1 - laboratorio di programmazione python.
#

# Funzione di controllo numero pari

def is_pari(n):
    """Ritorno vero se "n" è pari, se no ritorna falso """

    risultato = False

    if n%2 == 0 :
        risultato = True

    return risultato

##########

def main():
    numero = int(input('Dammi un numero: '))
    #print(type(numero))



    result = is_pari(numero)

    print(result)

main()



