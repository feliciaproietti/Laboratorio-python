
'''
#
# File: Programma.py
#
# Author: Felicia Proietti
#
# Date: 2026/03/03
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#
print('Hello, word')
'''

import turtle               # Importo modulo turtle

window = turtle.Screen()    # Creo una finestra dove lavorare
raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"

raffaello.color('red')

#for i in range(0, 4,1 ): #[0, 1, 2, 3]
for i in ['red', 'blue', 'violet', 'orange']:
 raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 50 passi
 raffaello.left(90)          # Dico a "raffaello" di girare a sinistra di 90 gradi

#raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 30 passi

#raffaello.left(90)          
#raffaello.forward(50)

#raffaello.left(90)          
#raffaello.forward(50)

#raffaello.left(90)# per tornare alla posizione iniziale

donatello=turtle.Turtle()
donatello.color('blue')
donatello.forward(50)
donatello.left(120) #devo mettere 120 per mettere il sistema di riferimento giusto
donatello.forward(50)
donatello.left(120)
donatello.forward(50)
donatello.left(120)

print(type(True))

window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma


