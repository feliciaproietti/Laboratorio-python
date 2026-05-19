#
# File: Esercizio7_definito.py
#
# Author: Felicia Proietti
#
# Date: 2026/05/12
#
# Version: 1.0
#
# Description: Esercizio 7 - laboratorio di programmazione python.
#


def generatore_tabellina(numero):
    """generatore infinito di multipli di 'numero'"""
    n = 0
    #loop infinito perché non mi serve fermarmi al 10
    while True:
        yield n*numero
        n = n +1
##############################

num = input('Con che numero desideri giocare?')
numero_intero = int(num)

print(f'Giocheremo con il numero {numero_intero}')
g = generatore_tabellina(numero_intero)
numero_tabellina = next(g)

continua = True 
while continua == True:    #equivalente a scrivere solo while continua:
    
    guess = input(f'il numero attuale è {numero_tabellina}. Qual è il prossimo numero?')

    #controllo se fermare il gioco
    if guess == 'FINE':
        continua = False
    
    numero_tabellina = next(g)

    if numero_tabellina == guess:
        print('hai indovinato!')

    else:
        print('riprova')


print('Esco dal gioco')
