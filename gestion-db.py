import tkinter as tk
from tkinter import messagebox
import creation_produit_graphic
import category_graphic
import modification_produit
import modification_category
import affichage_category
import affichage_produit
import suprime_category
import suprime_produit

class main :
    def creation_de_produit(self):
        creation_produit = creation_produit_graphic.creation_produit_graphic ()
        creation_produit.run ()

    def creation_de_category (self) :
        creation_category = category_graphic.creation_category_graphic ()
        creation_category.run ()

    def modification_de_produit (self) :
        modif_produit = modification_produit.modification_produit_graphic ()
        modif_produit.run ()

    def modification_de_category (self) :
        modif_produit = modification_category.modification_categgory_graphic ()
        modif_produit.run ()

    def affiche_produit (self) :
        affiche = affichage_produit.affichage ()
        affiche.run ()
    
    def affiche_category (self) :
        affiche = affichage_category.affichage ()
        affiche.run ()

    def suprime_prod (self) :
        sup = suprime_produit.suprime ()
        sup.run ()

    def suprime_cat (self) :
        sup = suprime_category.suprime ()
        sup.run ()


    def run (self) :

        # Create the main window
        root = tk.Tk()
        root.title("Text Input Example")

        # Set the window size to  800x600 pixels
        root.geometry('800x600')

        # Create a StringVar to hold the text input value
        text_var = tk.StringVar()


        # Create a Button that calls the submit function when clicked
        produit_button = tk.Button(root, text="creation de produit", command=self.creation_de_produit)
        produit_button.grid(row=1, column=0, columnspan=2)

        # Create a Button that calls the submit function when clicked
        category_button = tk.Button(root, text="creation de category", command=self.creation_de_category)
        category_button.grid(row=1, column=2, columnspan=2)

        # Create a Button that calls the submit function when clicked
        modif_produit_button = tk.Button(root, text="modification produit", command=self.modification_de_produit)
        modif_produit_button.grid(row=2, column=0, columnspan=2)  

        modif_category_button = tk.Button(root, text="modification category", command=self.modification_de_category)
        modif_category_button.grid(row=2, column=2, columnspan=2)  

        #button d'affichage
        affichage_produit = tk.Button(root, text="affiche produit", command=self.affiche_produit)
        affichage_produit.grid(row=3, column=0, columnspan=2)  

        affichage_category = tk.Button(root, text="affiche category", command=self.affiche_category)
        affichage_category.grid(row=3, column=2, columnspan=2)  

        boutton_suprime_produit = tk.Button(root, text="suprime produit", command=self.suprime_prod)
        boutton_suprime_produit.grid(row=4, column=0, columnspan=2)  

        boutton_suprime_category = tk.Button(root, text="suprime category", command=self.suprime_cat)
        boutton_suprime_category.grid(row=4, column=2, columnspan=2)  
        # Start the main event loop
        root.mainloop()

test = main ()
test.run ()