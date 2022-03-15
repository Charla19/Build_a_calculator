#Calculatrice avec les opérateurs de base en python

#Importation du module tkinter pour l'interface graphique
from tkinter import *


#la foncrion qui crée un évènement lors d'un clique
def clique(evenement) :
    global valeur
    text = event.widget.cget("text")
    if text == '=' :
        if valeur.get().isdigit():
            value = int(valeur.get())
        else:
            value = eval(screen.get())
        valeur.set(value)
        screen.update()
    elif text == 'C':
        valeur.set("")
        screen.update()
    else:
        valeur.set(valeur.get() + text)
        screen.update()

fenetre = Tk()

#définir la dimension de la fenêtre de l'interface
fenetre.geometry("500x600")

#Titre affichée en haut de l'interface
fenetre.title("Calculatrice basique")

#Couleur de fond de l'interface de la calculatrice
fenetre.config(bg="light blue")

valeur = StringVar()
valeur.set("")
f = Frame(fenetre, padx=15, pady=15)
screen = Entry(f, textvar = valeur, font = "Lucida 55 bold", bg = "light blue")
screen.pack(fill=X, padx=15, pady=15)
f.pack()

#La liste des options de boutons sur une ligne stocké dans un tableau
o1 = ["7","8","9","+"]
o2 = ["4","5","6","-"]
o3 = ["1","2","3","x"]
o4 = ["0","C","=","/"]

f = Frame(fenetre, bg="light blue", padx=10, pady=5)

#Methodes associées à l'option 1 "o1"
for i in o1:
    b = Button(f, text=i, padx=10, pady=5, font="Lucida 30 bold")
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-1>", clique)
f.pack()
f = Frame(fenetre, bg="light blue", padx=10, pady=5)

#Methodes associées à l'option 2 "o2"
for i in o2:
    b = Button(f, text=i, padx=10, pady=5, font="Lucida 30 bold")
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-2>", clique)
f.pack()
f = Frame(fenetre, bg="light blue", padx=10, pady=5)

#Methodes associées à l'option 3 "o3"
for i in o3:
    b = Button(f, text=i, padx=10, pady=5, font="Lucida 30 bold")
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-3>", clique)
f.pack()
f = Frame(fenetre, bg="light blue", padx=10, pady=5)

#Methodes associées à l'option 4 "o4"
for i in o4:
    b = Button(f, text=i, padx=10, pady=5, font="Lucida 30 bold")
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-4>", clique)
f.pack()
f = Frame(fenetre, bg="gray", padx=10, pady=5)

fenetre.mainloop()

