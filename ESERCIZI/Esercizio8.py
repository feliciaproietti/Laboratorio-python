#
# File: Esercizio8_definito.py
#
# Author: Felicia Proietti
#
# Date: 2026/05/19
#
# Version: 1.0
#
# Description: Esercizio 8 - laboratorio di programmazione python.
#

import random

def gioco_impiccato():
    # Lista di parole possibili
    parole = ["python", "programmazione", "computer", "sviluppatore", "algoritmo", "funzione"]
    
    # Selezione casuale della parola e inizializzazione delle variabili
    parola_segreta = random.choice(parole).lower()
    lettere_indovinate = set()
    lettere_sbagliate = set()
    tentativi_rimasti = 6

    print("--- Benvenuto al Gioco dell'Impiccato! ---")

    while tentativi_rimasti > 0:
        # Crea la visualizzazione corrente della parola (es. p _ t h o _ )
        visualizzazione = [lettera if lettera in lettere_indovinate else "_" for lettera in parola_segreta]
        print("\nParola da indovinare: " + " ".join(visualizzazione))
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        print(f"Lettere sbagliate: {', '.join(lettere_sbagliate) if lettere_sbagliate else 'Nessuna'}")

        # Controllo vittoria
        if "_" not in visualizzazione:
            print(f"\n🎉 Complimenti! Hai indovinato la parola: '{parola_segreta}'!")
            break

        # Input dell'utente con validazione
        tentativo = input("Inserisci una lettera: ").lower().strip()

        if len(tentativo) != 1 or not tentativo.isalpha():
            print("Per favore, inserisci una sola lettera valida.")
            continue

        if tentativo in lettere_indovinate or tentativo in lettere_sbagliate:
            print("Hai già provato questa lettera!")
            continue

        # Verifica se la lettera è corretta
        if tentativo in parola_segreta:
            print(f"Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"Peccato! La lettera '{tentativo}' non è presente.")
            lettere_sbagliate.add(tentativo)
            tentativi_rimasti -= 1

    else:
        print(f"\n💀 Hai esaurito i tentativi! La parola era: '{parola_segreta}'.")

# Per avviare il gioco basta chiamare la funzione:
gioco_impiccato()
