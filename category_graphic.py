import tkinter as tk
from tkinter import messagebox
import category

class creation_category_graphic :

    def submit(self):
        # Here you would process the data entered into the fields
        # Check if all fields are filled
        if not self.category_entrer_nom.get() :
            messagebox.showerror("Error", "Please fill out all fields.")
        else:
            category = category.category ()
            category.crea_category (self.category_entrer_nom.get())
            print("All fields are filled. Submit button clicked.")
            # You can also close the window after submitting
            self.root.destroy()
        print("Submit button clicked")

    def cancel(self):
        # Close the window without processing the data
        self.root.destroy()

    def run (self) :

        self.root = tk.Tk()
        self.root.title("produit Creation")

        # Set the window size to  800x600 pixels
        self.root.geometry('800x600')


        # Create labels and entry fields for produit information
        category_nom = tk.Label(self.root, text="produit Name")
        category_nom.pack()
        self.category_entrer_nom = tk.Entry(self.root)
        self.category_entrer_nom.pack()

        # Create submit and cancel buttons
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        cancel_button.pack()


        self.root.mainloop()

"""test = creation_category_graphic ()
test.run ()"""