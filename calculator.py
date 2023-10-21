import tkinter as tk
from tkinter import messagebox
import sys

def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

def calculate_stock_options(event=None):  # Add an event parameter
    lot_input = entry_lot.get()
    percentage_input = entry_percentage.get()
    price_input = entry_price.get()

    if not lot_input or not percentage_input:
        messagebox.showwarning("Warning", "Please enter values in both input fields.")
        return

    try:
        lot = float(lot_input)
        capital_increase_percentage = float(percentage_input)

        if lot == 0:
            raise ValueError("Number of stocks cannot be zero")
        if capital_increase_percentage == 0:
            raise ValueError("Percentage of capital increase cannot be zero")

        yeni_lot_sayisi = round(int(lot) * (1 + capital_increase_percentage / 100), 6)
        yeni_lot_sayisi_label.config(text=f"Yeni Lot Sayısı: {yeni_lot_sayisi:.6f}")

        options_list = []
        checker = 0

        while len(options_list) < 3:
            if is_int((lot + checker) * (1 + capital_increase_percentage / 100)):
                options_list.append(checker)
            checker += 1

        if price_input:
            try:
                price_of_one_share = float(price_input)
                total_price = round(price_of_one_share * lot, 2)
                options_label.config(text=f"Buy: {options_list} stocks to make it int. Total Price: {total_price:.2f}", fg="blue")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for Price of one share. Please enter a valid number.")
                return
        else:
            options_label.config(text=f"Buy: {options_list} stocks to make it int", fg="blue")

        options_label.grid(row=6, column=0, columnspan=2, pady=(10, 0), sticky='w')  # Left align options_label

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check your inputs")

def clear_inputs():
    entry_lot.delete(0, tk.END)
    entry_percentage.delete(0, tk.END)
    entry_price.delete(0, tk.END)

def quit_app():
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Stock Calculator")
root.geometry("420x320")  # Set the window size to 420x320
root.resizable(0, 0)  # Make the window non-resizable

# Create and place widgets in the window
label_lot = tk.Label(root, text="Number of Stocks:")
label_lot.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')  # Align left

entry_lot = tk.Entry(root)
entry_lot.grid(row=0, column=1, padx=10, pady=(10, 0))

label_percentage = tk.Label(root, text="Percentage of Capital Increase:")
label_percentage.grid(row=1, column=0, padx=10, sticky='w')  # Align left

entry_percentage = tk.Entry(root)
entry_percentage.grid(row=1, column=1, padx=10)

label_price = tk.Label(root, text="Price of one share (optional):")
label_price.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')  # Align left

entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_stock_options, bg="dark orange", bd=0)
calculate_button.grid(row=3, column=0, columnspan=1, pady=10, sticky='e')  # Align calculate_button to the right

clear_button = tk.Button(root, text="Clear", command=clear_inputs, bg="red", bd=0)
clear_button.grid(row=3, column=1, columnspan=1, pady=10, sticky='w')  # Align clear_button to the left

yeni_lot_sayisi_label = tk.Label(root, text="", fg="blue")
yeni_lot_sayisi_label.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky='w')  # Left align yeni_lot_sayisi_label

options_label = tk.Label(root, text="Options:")
options_label.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')  # Left align options_label

options_label.grid_remove()  # Hide options_label initially

# Bind the <Return> event to the root window
root.bind("<Return>", calculate_stock_options)

# Function to properly close the application
def on_closing():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)  # Call on_closing when closing the window

# Menu for macOS
if sys.platform == 'darwin':
    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Quit", command=quit_app)

# Start the GUI event loop
root.mainloop()
