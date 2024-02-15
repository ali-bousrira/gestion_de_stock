import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import category

class modification_categgory_graphic :
    def submit(self):
        if not self.category_entrer_nom.get () :
            messagebox.showerror("Error", "Please fill out all fields.")
        else:
            selected_index = self.listbox.curselection()
            if selected_index:
                selected_index_number = selected_index[0]
                modif_category = category.modification()
                modif_category.modif(self.category_entrer_nom.get (), int (self.data_category[selected_index_number][0]))
                print("All fields are filled. Submit button clicked.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Please select an item from the list.")

    def cancel(self):
        self.root.destroy()


    def run (self) :
        self.root = tk.Tk()
        self.root.title("produit Creation")

        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        self.root.geometry('800x600')


        scrollbar = ttk.Scrollbar(frame,)
        scrollbar.pack(side='right', fill='y')

        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side='left', fill='both', expand=True)

        scrollbar.config(command=self.listbox.yview)

        manip_categ = category.manipulation_category ()
        self.data_category = manip_categ.read ()
        for i in range(len (self.data_category)):
            self.listbox.insert('end', f"Item {self.data_category[i]}")


        category_nom = tk.Label(self.root, text="nouveau nom de la category")
        category_nom.pack()
        self.category_entrer_nom = tk.Entry(self.root)
        self.category_entrer_nom.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        cancel_button.pack()

        self.root.mainloop()

"""test = modification_categgory_graphic ()
test.run ()"""