import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from produit import crea_produit
import category

class suprime :

    def submit(self):
        # Here you would process the data entered into the fields
        # Check if all fields are filled

        # All fields are filled, proceed with the submission
        selected_index = self.listbox.curselection()
        if selected_index:  # Check if there is a selection
            selected_index_number = selected_index[0]  # Get the index number of the first selected item
            selected_label = self.listbox.get(selected_index)
            print("Selected index number:", selected_index_number)
            print("Selected label:", selected_label)
            # Now you can use the selected_index_number variable for further processing
            # For example, pass it to the crea_produit function
            outil_suprime = category.suprime ()
            outil_suprime.run (self.data_category[selected_index_number][0])

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

        # Create submit and cancel buttons
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        cancel_button.pack()

        self.root.mainloop()


"""test = suprime ()
test.run ()"""
