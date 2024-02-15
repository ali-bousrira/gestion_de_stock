import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from produit import crea_produit
import category

class modification_produit_graphic :

    def submit(self):
        # Here you would process the data entered into the fields
        # Check if all fields are filled
        if not self.produit_entrer_nom.get() or not self.produit_entrer_discription.get() or not self.produit_entrer_prix.get() or not self.produit_entrer_quantites.get() or not self.produit_entrer_id.get ():
            messagebox.showerror("Error", "Please fill out all fields.")
        else:
            # All fields are filled, proceed with the submission
            selected_index = self.listbox.curselection()
            if selected_index:  # Check if there is a selection
                selected_index_number = selected_index[0]  # Get the index number of the first selected item
                selected_label = self.listbox.get(selected_index)
                print("Selected index number:", selected_index_number)
                print("Selected label:", selected_label)
                # Now you can use the selected_index_number variable for further processing
                # For example, pass it to the crea_produit function
                modif_produit = crea_produit()
                modif_produit.modif(self.produit_entrer_nom.get(), self.produit_entrer_discription.get(), int (self.produit_entrer_prix.get()), int (self.produit_entrer_quantites.get()), self.data_category[selected_index_number][0], int (self.produit_entrer_id.get ()))
                print("All fields are filled. Submit button clicked.")
                # You can also close the window after submitting
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Please select an item from the list.")

    def cancel(self):
        # Close the window without processing the data
        self.root.destroy()

    def run (self):
            

        self.root = tk.Tk()
        self.root.title("produit Creation")

        # Create a frame to contain the listbox and scrollbar
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        # Set the window size to  800x600 pixels
        self.root.geometry('800x600')


        # Create labels and entry fields for produit information
        produit_text_id = tk.Label(self.root, text="id de produit")
        produit_text_id.pack()
        self.produit_entrer_id = tk.Entry(self.root)
        self.produit_entrer_id.pack()

        produit_text_nom = tk.Label(self.root, text="nom produit")
        produit_text_nom.pack()
        self.produit_entrer_nom = tk.Entry(self.root)
        self.produit_entrer_nom.pack()

        produit_text_discription = tk.Label(self.root, text="Discription")
        produit_text_discription.pack()
        self.produit_entrer_discription = tk.Entry(self.root)
        self.produit_entrer_discription.pack()

        produit_text_prix = tk.Label(self.root, text="Price entier")
        produit_text_prix.pack()
        self.produit_entrer_prix = tk.Entry(self.root)
        self.produit_entrer_prix.pack()

        produit_text_quantites = tk.Label(self.root, text="quantites entier")
        produit_text_quantites.pack()
        self.produit_entrer_quantites = tk.Entry(self.root)
        self.produit_entrer_quantites.pack()



        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(frame,)
        scrollbar.pack(side='right', fill='y')

        # Create a listbox and attach the scrollbar to it
        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side='left', fill='both', expand=True)

        # Configure the scrollbar to update the listbox view
        scrollbar.config(command=self.listbox.yview)

        # Populate the listbox with items
        manip_categ = category .manipulation_category ()
        self.data_category = manip_categ.read ()
        for i in range(len (self.data_category)):
            self.listbox.insert('end', f"Item {self.data_category[i]}")

        # Create submit and cancel buttons
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        cancel_button.pack()

        self.root.mainloop()


"""test = creation_produit_graphic ()
test.run ()"""