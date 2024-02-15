import tkinter as tk
from tkinter import ttk
import category

class affichage :
    def run (self):
            

        self.root = tk.Tk()
        self.root.title("produit Creation")

        # Create a frame to contain the listbox and scrollbar
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        # Set the window size to  800x600 pixels
        self.root.geometry('800x600')


        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(frame,)
        scrollbar.pack(side='right', fill='y')

        # Create a listbox and attach the scrollbar to it
        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side='left', fill='both', expand=True)

        # Configure the scrollbar to update the listbox view
        scrollbar.config(command=self.listbox.yview)

        # Populate the listbox with items
        manip_categ = category.manipulation_category ()
        self.data_category = manip_categ.read ()
        for i in range(len (self.data_category)):
            self.listbox.insert('end', f"Item {self.data_category[i]}")


        self.root.mainloop()

"""test = affichage ()
test.run ()"""